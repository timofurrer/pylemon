# -*- coding: utf-8 -*-

import os
import yaml

from logger import Logger
from directoryhandler import DirectoryHandler
from monitor import Monitor


class Config(object):
    def __init__(self):
        self._logger = Logger()
        self._directories = []

    def parse(self, filename):
        if not os.path.exists(filename):
            self._logger.error("config file %s does not exist" % filename)
            return False

        with open(filename, "r") as f:
            content = yaml.load(f)

        monitor = content["monitor"]

        for k, v in monitor.iteritems():
            d = DirectoryHandler(k)
            self._parse_actions(d, v)

        return True

    def _parse_actions(self, directory, actions):
        try:
            directory.register_event(Monitor.CREATE, actions["create"])
        except KeyError:
            pass

        try:
            directory.register_event(Monitor.DELETE, actions["delete"])
        except KeyError:
            pass

        try:
            directory.register_event(Monitor.MODIFY, actions["modify"])
        except KeyError:
            pass

        self._directories.append(directory)

    def get_directories(self):
        return self._directories
