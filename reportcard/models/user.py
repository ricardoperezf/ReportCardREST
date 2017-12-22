#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from passlib.apps import custom_app_context as pwd_context
from reportcard import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hashed = db.Column(db.String(64))

    def __init__(self, username):
        self.username = username
        
    def hash(self, password):  # ENCRYPTAR LA CONTRASEÑA.
        self.password_hashed = pwd_context.encrypt(password)
