# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:05:11 2019

@author: bianl
"""
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from flask_script import Manager,Server

app = Flask(__name__)
#  开启debug模式
Manager(app).add_command("runserver", Server(use_debugger=True))
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'
toolbar = DebugToolbarExtension( app )  

engine = create_engine('mysql+pymysql://root@localhost/py2db', echo=True)
db = scoped_session(sessionmaker(bind = engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("PyDb_index.html",flights=flights)

@app.route("/book",methods=["POST"])
def book():
    """  Book a flight.  """
    
    #  Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",message="Invalid flight number.")
    
    #  Make sure the flight exists.
    if db.execute("SELECT * FROM flights WHERE id=:id",{"id":flight_id}).rowcount == 0:
        return render_template("error.html",message="No such flight with that id")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",{"name":name,"flight_id":flight_id})
    db.commit()
    return render_template("PyDb_success.html")

@app.route("/flights")
def flights():
    """   Lists all flights.  """
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("PyDb_flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight( flight_id ):
    """  Lists details about a single flight.  """
    
    #  Make sure flight exist
    flight = db.execute("SELECT * FROM flights WHERE id=:id",{"id":flight_id}).fetchone()
    if flight is None:
         return render_template("error.html",message="No such flight.")   
    
    #  Get all passengers.
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id":flight_id}).fetchall()    
        
    return render_template("PyDb_flight.html",flight=flight,passengers=passengers)

if __name__ == "__main__":   
    Manager(app).run()