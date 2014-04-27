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

    def process_IN_CREATE(self, event):
        self._is_registered(event)
        self._logger.info("created %s" % event.pathname)
        self._execute_action(event)

    def process_IN_MODIFY(self, event):
        self._is_registered(event)
        self._logger.info("modified %s" % event.pathname)
        self._execute_action(event)

    def process_IN_DELETE(self, event):
        self._is_registered(event)
        self._logger.info("deleted %s" % event.pathname)
        self._execute_action(event)

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
