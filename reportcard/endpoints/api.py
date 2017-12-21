#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

reportcard_app = Flask(__name__)
reportcard_app.config['SECRET_KEY'] = 'abcdefgh'
reportcard_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
reportcard_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(reportcard_app)

vector_grades = {'nombre': 'Ricardo', 'course': 'Web Services', 'grade': 100}


@reportcard_app.route('/')
def hello_world():
    return 'Hello from Flask! Im RicDev'


@reportcard_app.route('/grades')
def get_grades():
    global vector_grades
    return "<h1>Nombre: %s</h1>" % vector_grades['nombre']


@reportcard_app.route('/register', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    if user.User.query.filter_by(username=username).first() is not None:
        abort(400)  # existing user
    new_user_db = user.User(username=username)
    new_user_db.hash(password)
    db.session.add(new_user_db)
    db.session.commit()
    return jsonify({'username': new_user_db.username}), 201


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        user.db.create_all()
    reportcard_app.run(host="0.0.0.0", port=5000)
