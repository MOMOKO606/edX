# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:05:39 2018

@author: bianl
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)                 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)
    

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')