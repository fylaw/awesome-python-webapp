#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'y'

import os, re
from datetime import datetime

from fabric2.connection import Connection
from invoke import task

# 服务器用户
#env.user = 'root'
#env.sudo_user='root'
#env.hosts=['118.24.152.189']

# mysql用户名密码
db_user = 'root'
db_password = 'dkstFeb.1st'


_TAR_FILE = 'dist-awesome.tar.gz'

@task
def build(c):
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    Connection.local('rm -f dist/%s' % _TAR_FILE)
    with Connection.cd(os.path.join(os.path.abspath(''), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        Connection.local(' '.join(cmd))