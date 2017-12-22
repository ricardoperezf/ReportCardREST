#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append('/home/ricardo/ws/ReportCard/ReportCard/reportcard/')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context

reportcard_app = Flask(__name__)
reportcard_app.config['SECRET_KEY'] = 'abcdefgh'
reportcard_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
reportcard_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(reportcard_app)

from reportcard.endpoints import *
from reportcard.model import *
