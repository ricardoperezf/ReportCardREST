#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

vector_grades = {'nombre': 'Ricardo', 'course': 'Web Services', 'grade': 100}


@app.route('/')
def hello_world():
    return 'Hello from Flask! Im RicDev'


@app.route('/grades')
def get_grades():
    global vector_grades
    return "<h1>Nombre: %s</h1>" % vector_grades['nombre']


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
