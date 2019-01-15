# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 18:04:04 2019

@author: bianl
"""

import datetime
from flask import Flask, render_template

app = flask( __name__ )
@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    render_template("index.html", new_year = new_year)