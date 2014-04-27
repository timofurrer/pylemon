# -*- coding: utf-8 -*-

import sys
import syslog
from singleton import singleton

@singleton()
class Logger(object):
    PRIORITIES = {"debug": syslog.LOG_DEBUG, "info": syslog.LOG_INFO, "notice": syslog.LOG_NOTICE, "warning": syslog.LOG_WARNING, "error": syslog.LOG_ERR, "emerg": syslog.LOG_EMERG}

    def __init__(self):
        self._stderr = open("/var/log/pylemon.stderr", "w+")
        self._stdout = open("/var/log/pylemon.stdout", "w+")
        syslog.openlog("pylemon")

    def __del__(self):
        syslog.closelog()
        self._stdout.close()
        self._stderr.close()

    def __getattr__(self, attr):
        try:
            prio = Logger.PRIORITIES[attr]
            def _wrapper(msg):
                syslog.syslog(prio, msg)
            return _wrapper
        except KeyError:
            raise AttributeError("Logger has not log priority %s" % attr)

    def redirect_std(self):
        sys.stdout = self._stdout
        sys.stderr = self._stderr

    def get_stdout(self):
        return self._stdout

    def get_stderr(self):
        return self._stderr
