# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:44:20 2019

@author: bianl
"""

from flask import Flask,render_template, request

app = Flask( __name__ )

@app.route("/")
def index():
    return render_template("index1.html")
    
@app.route("/hello", methods=["POST"])
def hello():
    if(request.method == "GET"):
        return " Please submit the form instead "
    else:
        name = request.form.get("name")
        return render_template("hello.html",name=name)