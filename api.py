#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

if __name__ == '__main__':
  app.run(debug = True)