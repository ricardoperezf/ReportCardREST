#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

reportcard_app = Flask(__name__)
reportcard_app.config['SECRET_KEY'] = 'abcdefgh'
reportcard_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
reportcard_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(reportcard_app)

from reportcard.endpoints import *
