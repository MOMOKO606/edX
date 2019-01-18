# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:43:58 2019

@author: bianl
"""

from flask import Flask

app = Flask( __name__ )

@app.route("/")
def Hello_index():
    return "Hello,World!"

@app.route("/<string:name>")
def sayhello(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run( debug = True)