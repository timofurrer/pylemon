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
            try:
                file_actions = v["onfile"]
                self._parse_actions(d, file_actions)
            except KeyError:
                pass

            try:
                dir_actions = v["ondir"]
                self._parse_actions(d, dir_actions, ondir=True)
            except KeyError:
                pass

        return True

    def _parse_actions(self, directory, actions, ondir=False):
        dirmask = Monitor.ISDIR if ondir else 0x00
        try:
            directory.register_event(Monitor.CREATE | dirmask, actions["create"])
        except KeyError:
            pass

        try:
            directory.register_event(Monitor.DELETE | dirmask, actions["delete"])
        except KeyError:
            pass

        try:
            directory.register_event(Monitor.MODIFY | dirmask, actions["modify"])
        except KeyError:
            pass

        self._directories.append(directory)

    def get_directories(self):
        return self._directories
