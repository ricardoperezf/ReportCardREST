#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import user

app = Flask(__name__)

vector_grades = {'nombre': 'Ricardo', 'course': 'Web Services', 'grade': 100}

def example():
    return 10

@app.route('/')
def hello_world():
    return 'Hello from Flask! Im RicDev'


@app.route('/grades')
def get_grades():
    global vector_grades
    return "<h1>Nombre: %s</h1>" % vector_grades['nombre']


@app.route('/register')
def register_new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    print("\n" + str(username) + " " + str(password) + "\n")
    if username is None or password is None:
        abort(400)  # MISSING USERNAME OR PASSWORD.
    if user.User.query.filter_by(username=username).first() is not None:
        abort(400)  # ALREADY EXISTING USER.
    new_user = user.User(username=username)
    new_user.hash(password)
    user.db.session.add(user)
    user.db.session.commit()
    return jsonify({'username': user.username}), 201


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
