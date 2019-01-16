# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:28:59 2019

@author: bianl
"""
import datetime
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

@app.route("/newyear")
def isnewyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("NewYear.html", new_year = new_year)

@app.route("/namelist")
def namelist():
    names = ["Bianlong","Liuying","Bianyanxi"]
    return render_template("namelist.html",names = names)


if (__name__ == "__main__"):
    app.run( debug = True )