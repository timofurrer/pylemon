#!/usr/bin/python
# -*- coding: utf-8 -*-

from imp import load_source
from setuptools import setup

version = load_source("version", "pylemon/__init__.py")

setup(
    name="pylemon",
    version=version.__version__,
    license="MIT",
    description="python daemon to monitor specific directories and react on changes",
    author="Timo Furrer",
    author_email="tuxtimo@gmail.com",
    maintainer="Timo Furrer",
    maintainer_email="tuxtimo@gmail.com",
    platforms=["Linux"],
    url="http://github.com/timofurrer/pylemon",
    download_url="http://github.com/timofurrer/pylemon",
    install_requires=["pysingleton"],
    packages=["pylemon"],
    entry_points={"console_scripts": ["pylemon = pylemon.main:main"]},
    package_data={"pylemon": ["*.md"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: Implementation"
    ],
)
