#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from reportcard import db
from sqlalchemy import Date


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(32), index=True)
    grade = db.Column(db.String(32), index=True)
    date = db.Column(db.String(32), index=True)

    def __init__(self, course, grade, date):
        self.course = course
        self.grade = grade
        self.date = date
