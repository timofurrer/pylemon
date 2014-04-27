# -*- coding: utf-8 -*-

from pyinotify import WatchManager, Notifier, ALL_EVENTS, IN_CREATE, IN_DELETE, IN_MODIFY, IN_ISDIR

from logger import Logger


class Monitor(object):
    ALL = ALL_EVENTS
    CREATE = IN_CREATE
    DELETE = IN_DELETE
    MODIFY = IN_MODIFY
    ISDIR = IN_ISDIR

    def __init__(self, config):
        self._config = config
        self._logger = Logger()
        self._watchManager = WatchManager()
        self._notifier = Notifier(self._watchManager)

    def watch_config(self):
        for d in self._config.get_directories():
            self.watch(d)

    def watch(self, directory):
        self._logger.info("watching directory %s" % directory.get_path())
        self._watchManager.add_watch(directory.get_path(), directory.get_eventmask(), proc_fun=directory)

    def run(self):
        self._logger.info("start monitor loop")
        self._notifier.loop()
