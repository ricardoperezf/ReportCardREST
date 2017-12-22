#!/usr/bin/python
# -*- coding: utf-8 -*-
from reportcard import db


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(32), index=True)
    grade = db.Column(db.String(32), index=True)

    def __init__(self, course, grade):
        self.course = course
        self.grade = grade
