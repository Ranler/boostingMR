#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from flask import Flask
from flaskext.actions import Manager
from boostingMR import app


manager = Manager(app)

if __name__ == "__main__":
    app.debug = True
    manager.run()

