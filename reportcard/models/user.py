#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append("/home/ricardo/ws/ReportCard/ReportCard/reportcard")
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from reportcard import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hashed = db.Column(db.String(64))

    def hash(self, password):  # ENCRYPTAR LA CONTRASEÑA.
        self.password_hashed = pwd_context.encrypt(password)
