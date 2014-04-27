# -*- coding: utf-8 -*-

from pyinotify import ProcessEvent
from subprocess import Popen, PIPE

from logger import Logger
from monitor import Monitor


class DirectoryHandler(ProcessEvent):
    def __init__(self, path):
        self._logger = Logger()
        self._path = path
        self._eventmask = 0x00
        self._events = {}

    def get_path(self):
        return self._path

    def get_eventmask(self):
        return self._eventmask

    def register_event(self, event, action):
        self._eventmask |= event
        self._events[event] = action
        self._events[event | Monitor.ISDIR] = action

    def _is_registered(self, event):
        if event.mask not in self._events:
            self._logger.error("no action %s registered for directory %s" % (event.maskname, event.path))
            return False
        return True

    def __getattr__(self, attr):
        if attr.startswith("process_IN_"):
            def _process_wrapper(event):
                self._is_registered(event)
                self._logger.info("%s %s" % (event.maskname, event.pathname))
                self._execute_action(event)
            return _process_wrapper
        raise AttributeError("no attribute %s found in DirectoryHandler" % attr)

    def _execute_action(self, event):
        action = self._events[event.mask]
        self._logger.info("execute %s for event %s on %s" % (action, event.maskname, event.path))
        try:
            command = action.split()
            command.append(event.path)
            command.append(event.pathname)
            command.append("1" if event.dir else "0")
            process = Popen(command, stdout=PIPE, stderr=PIPE)
        except Exception, e:
            self._logger.error("cannot execute %s because '%s'" % (action, str(e)))
            return False

        process.wait()
        if process.returncode != 0:
            self._logger.warning("execution of %s ended with failure return code %d" % (action, process.returncode))
        return True
