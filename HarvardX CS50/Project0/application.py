# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:28:59 2019

@author: bianl
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello!"
    return render_template("index.html",headline = headline)

@app.route("/bye")
def bye():
    headline = "Bye!"
    return render_template("index.html",headline = headline)

if (__name__ == "__main__"):
    app.run( debug = True )