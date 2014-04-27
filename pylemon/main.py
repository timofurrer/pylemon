#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logger import Logger
from config import Config
from monitor import Monitor


def main():
    logger = Logger()
    logger.redirect_std()
    logger.info("started pylemon daemon")

    config = Config()
    config.parse("/etc/pylemon.conf")

    monitor = Monitor(config)
    monitor.watch_config()
    monitor.run()

if __name__ == "__main__":
    main()
