# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:49:03 2019

@author: bianl
"""
from flask import Flask,render_template,request,session
from flask_session import Session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask( __name__ )
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'
toolbar = DebugToolbarExtension( app )  

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def p1():
    return render_template("S_page1.html")

@app.route("/page2")
def p2():
    return render_template("S_page2.html")

@app.route("/form",methods=["POST"])
def form():
    if session.get("strlist") is None:
        session["strlist"] = []
    else:
        newstr = request.form.get("name")
        strlist = session.get("strlist")
        strlist.append(newstr)
    return render_template("FormPractice.html",strlist = strlist)
