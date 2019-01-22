# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:52:01 2019

@author: bianl
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker  

engine = create_engine('mysql+pymysql://root@localhost/py2db', echo=True)
db = scoped_session(sessionmaker(bind = engine))

def main():
    #  List all flights.
    flights = db.execute("SELECT id,origin,destination,duration FROM flights")
    for flight in flights:
        print(f"Flight {flight.id}:{flight.origin} to {flight.destination},{flight.duration} minutes.")
        
    #  Prompt user to choose a flight
    flight_id = int(input("\nFlight ID:"))
    flight = db.execute("SELECT origin,destination,duration FROM flights WHERE id=:id",{"id":flight_id}).fetchone()
    
    #  Make sure flight is valid
    if flight is None:
        print("Error:No such flight.")
        return
    
    #  List passengers.
    passengers = db.execute("SELECT name FROM  passengers WHERE flight_id=:flight_id",{"flight_id":flight_id}).fetchall()
    print("\nPassengers:")
    if len(passengers) == 0:
        print("No passengers.")
    for passenger in passengers:
        print(passenger.name)

if __name__ == "__main__":
    main()
            
    