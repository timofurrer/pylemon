#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

from logger import Logger
from config import Config
from monitor import Monitor


def main():
    logger = Logger()
    logger.redirect_std()
    logger.info("started pylemon daemon")

    config = Config()
    if not config.parse("/etc/pylemon.conf"):
        logger.error("abort pylemon because of failure during config parse")
        exit(1)

    monitor = Monitor(config)
    monitor.watch_config()
    monitor.run()

if __name__ == "__main__":
    main()
