# pylemon
> python file monitor <br>
> python daemon to monitor specific directories and react on changes

***

**Author:** Timo Furrer <tuxtimo@gmail.com> <br>
**Version:** 0.00.01 <br>
**License:** MIT <br>

## How to install

### Dependencies
First you have to install some dependencies:

    apt-get install python-pyinotify python-yaml

*Note: you need root privileges*

### Install pylemon
There is a Makefile which installs the python daemon and a System V script.

    make install

*Note: you need root privileges*

## Start/Stop and Status
The `pylemon daemon` will automatically startup on system start and load the config file from `/etc/pylemon.conf` <br>

### Manual start

    service pylemon start

### Manual stop

    service pylemon stop

### Manual restart

    service pylemon restart

### Get current status

    service pylemon status


## Logging
The `pylemon daemon` logs to `syslog`. You can watch it with:

    tail -F /var/log/syslog

The stdout and stderr of the daemon are redirected to `/var/log` and can be watched with:

    tail -F /var/log/pylemon.stdout
    tail -F /var/log/pylemon.stderr

## Write config file

The config file must be located at `/etc/pylemon.conf`. It can be a symlink of course.
The config file syntax is like the following:

    monitor:
      <somedirectory>
        onfile:
          create: /example/create_hook_script
          delete: /example/delete_hook_script
          modify: /example/modify_hook_script
        ondir:
          create: /example/create_hook_script
          delete: /example/delete_hook_script
          modify: /example/modify_hook_script
      <someotherdirectory>
        ...
