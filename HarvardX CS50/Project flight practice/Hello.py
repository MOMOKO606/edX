# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:08:04 2019

@author: bianl
"""
from flask import Flask,render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'
toolbar = DebugToolbarExtension( app )  

@app.route("/")
def index():
    return render_template( "H_index.html" )

@app.route("/<string:name>")
def Hello2U( name ):
    name = name.capitalize()
    return render_template( "H_Hello2U.html",name = name )


if __name__ == "__main__":   
    app.run()
