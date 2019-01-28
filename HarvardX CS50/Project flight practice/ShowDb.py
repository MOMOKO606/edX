# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:56:53 2019

@author: bianl
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

""" Connecting the Database."""
engine = create_engine( "mysql+pymysql://root@localhost/Py2Db",echo = True )
db = scoped_session(sessionmaker(bind = engine))

"""Show all the flights."""
flights = db.execute("SELECT * FROM flights").fetchall()
for flight in flights:
    print(f"{flight.id}.{flight.origin} to {flight.destination}, {flight.duration} mins")

"""Let the user choose a ID."""
flight_id = input("Pleasa enter a flight ID:")
flight = db.execute("SELECT * FROM flights WHERE id = :flight_id",{'flight_id':flight_id}).fetchone()
print(f"You've selected the flight from {flight.origin} to {flight.destination}, flight_id:{flight.id}, passengers:")

"""Get the relative passengers information."""
passengers = db.execute("SELECT * FROM passengers WHERE flight_id = :flight_id",{'flight_id':flight_id}).fetchall()
for passenger in passengers:
    print( passenger.name )
