#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manage
    ~~~~~~

    Set of some useful management commands.

"""

import subprocess
from flask.ext.script import Server, Shell, Manager
from app import app
from libs.ext import db


manager = Manager(app)


@manager.command
def clean_pyc():
    """Removes all *.pyc files from the project folder"""
    clean_command = "find . -name *.pyc -delete".split()
    subprocess.call(clean_command)


@manager.command
def init_data():
    """Fish data for project"""
    db.drop_all()
    db.create_all()

#    user = User(username='John Doe', email='john@doe.com', password='test')
#    user.save()


manager.add_command('shell', Shell(make_context=lambda:{'app': app, 'db': db}))

server = Server(host="0.0.0.0", port=8777)
manager.add_command("runserver", server)


if __name__ == '__main__':
    manager.run()
