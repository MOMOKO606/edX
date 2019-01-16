# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:14:47 2019

@author: bianl
"""

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def page1():
    return render_template("page1.html")

@app.route("/p2")
def page2():
    return render_template("page2.html")