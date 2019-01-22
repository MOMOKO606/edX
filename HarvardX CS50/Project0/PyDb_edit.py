# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:29:52 2019

@author: bianl
"""
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker  

engine = create_engine('mysql+pymysql://root@localhost/py2db', echo=True)
db = scoped_session(sessionmaker(bind = engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin,destination,duration in reader:
        db.execute("INSERT INTO flights (origin,destination,duration) VALUES (:origin,:destination,:duration)",
                  {'origin':origin,'destination':destination,'duration':duration})
        print( f"Added flight from {origin} to {destination} lasting {duration} mintues")
    db.commit()
        
if __name__ == "__main__":
    main()
   