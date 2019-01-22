# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:36:02 2019

@author: bianl
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker  

engine = create_engine('mysql+pymysql://root@localhost/py2db', echo=True)
db = scoped_session(sessionmaker(bind = engine))

def main():
    flights = db.execute("SELECT origin,destination,duration from flights")
    for flight in flights:
        print( f"{flight.origin} to {flight.destination},{flight.duration} minutes.")
    
    
if __name__ == "__main__":
    main()