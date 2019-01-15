# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:31:50 2019

@author: bianl
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello,world!"

@app.route("/<string:name>")
def hello(name):
    return f"Hello,{name}!"

if __name__ == '__main__':
      app.run()
