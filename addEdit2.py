from cgitb import reset
from tracemalloc import start
from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint
import json
# from Project0 import greeting
import sys
from datetime import datetime, timedelta
import calendar
from colorama import init
from termcolor import colored
import pandas as pd
from dateutil.parser import parse
import parser



def add_class2():

    client = MongoClient('mongodb://localhost:27017')
    db = client.project0
    col = db['class02']

    entryData = {}
    while (True):
        print("_____________________________________")
        className = input('Enter your Class Name: ')
        print('Saved class ' + className)
        entryData["className"] = className

        if (className == ""):
            print('Please enter your Class Name: ')
            
        startDate = input("What date does this class start? /n ex MM/DD/YYYY: ") 
        format = '%m/%d/%Y'
        check = True
        try:
            check = bool(datetime.strptime(startDate, format))
            
            """End Date Try...Except"""
            endDate = input("What date does this class end? /n ex MM/DD/YYYY: ") 
            format = '%m/%d/%Y'
            checkEnd = True
            try:
                checkEnd = bool(datetime.strptime(endDate, format))
                entryData["classDate"] = {}
                entryData["classDate"]["startDate"] = startDate
                entryData["classDate"]["endDate"] = endDate
                entryWeekday = AgendaMenu(    
                    {
                        1 : "Monday",
                        2 : "Tuesday",
                        3 : "Wednesday",
                        4 : "Thursday",
                        5 : "Friday",
                        6 : "Saturday"
                        }
                    )
                entryWeekday.printAgendaMenu()
                resultWeekday = entryWeekday.menuResponse("Please enter the number corresponding with you events date. ")
                resultWeekday = datetime.strptime(resultWeekday,"%A").date()
                changeWeekday = resultWeekday.weekday()
                # weekdayResult = [resultWeekday for resultWeekday in pd.date_range(start = startDate, end = endDate)if resultWeekday.weekday() in [changeWeekday]]
                # entryData["weekday"] = changeWeekday
                """Class Time Try... Except"""
                classTime = input("Enter the hour your class starts. /n ex 09:05AM or 09:05PM: ")
                format = '%I:%M%p'
                checkTime = True
                try:
                    checkTime = bool(datetime.strptime(classTime, format))
                    entryData["classTime"] = classTime 
                    timeStringStart = str(startDate + " " + classTime)
                    timeStringEnd = str(endDate + " " + classTime)
                    classRepeat = [resultWeekday for resultWeekday in pd.date_range(start = timeStringStart, end = timeStringEnd)if resultWeekday.weekday() in [changeWeekday]]
                    entryData["repeat"] = classRepeat
                    print(entryData)
                    # entryData_id = col.insert_one(entryData).inserted_id
                    # print({entryData_id})
                except:
                    """Except for classTime"""
                    checkTime = False
                    print("Please type response as /n ex 9:05AM or 9:05PM: ")
            except ValueError: 
                """Except for endDate"""      
                checkEnd = False
                print("Please type response as MM/DD/YYYY")
        except ValueError:
            """Except for startDate"""          
            check = False
            print("Please type response as MM/DD/YYYY")
if(__name__) == "__main__":
    add_class2()
         
def add_event2():

    client = MongoClient('mongodb://localhost:27017')
    db = client.project0
    col = db['event02']

    entryData = {}
    while (True):
        print("_____________________________________")
        eventName = input('Enter your Event Name: ')
        print('Saved event ' + eventName)
        entryData["eventName"] = eventName

        if (eventName == ""):
            print('Please enter your Event Name: ')
            
        startDate = input("What date does this class start? /n ex MM/DD/YYYY: ") 
        format = '%m/%d/%Y'
        check = True
        try:
            check = bool(datetime.strptime(startDate, format))
            
            """End Date Try...Except"""
            endDate = input("What date does this class end? /n ex MM/DD/YYYY: ") 
            format = '%m/%d/%Y'
            checkEnd = True
            try:
                checkEnd = bool(datetime.strptime(endDate, format))
                entryData["eventDate"] = {}
                entryData["eventDate"]["startDate"] = startDate
                entryData["eventDate"]["endDate"] = endDate
                entryWeekday = AgendaMenu(    
                    {
                        1 : "Monday",
                        2 : "Tuesday",
                        3 : "Wednesday",
                        4 : "Thursday",
                        5 : "Friday",
                        6 : "Saturday"
                        }
                    )
                entryWeekday.printAgendaMenu()
                resultWeekday = entryWeekday.menuResponse("Please enter the number corresponding with you events date. ")
                # resultWeekday = datetime.strptime(resultWeekday,"%A").date()
                changeWeekday = resultWeekday.weekday()
                entryData["weekday"] = resultWeekday
                """Event Time Try... Except"""
                eventTime = input("Enter the hour your class starts. /n ex 09:05AM or 09:05PM: ")
                format = '%I:%M%p'
                checkTime = True
                try:
                    checkTime = bool(datetime.strptime(eventTime, format))
                    entryData["eventTime"] = eventTime
                    timeStringStart = str(startDate + " " + eventTime)
                    timeStringEnd = str(endDate + " " + eventTime)
                    eventRepeat = [resultWeekday for resultWeekday in pd.date_range(start = timeStringStart, end = timeStringEnd)if resultWeekday.weekday() in [changeWeekday]]
                    entryData["repeat"] = eventRepeat
                    print(entryData)
                    # entryData_id = col.insert_one(entryData).inserted_id
                    # print({entryData_id})
                except:
                    """Except for eventTime"""
                    checkTime = False
                    print("Please type response as /n ex 9:05AM or 9:05PM: ")
            except ValueError: 
                """Except for endDate"""      
                checkEnd = False
                print("Please type response as MM/DD/YYYY")
            print(entryData)
            entryData_id = col.insert_one(entryData).inserted_id
            print({entryData_id})
        except ValueError:
            """Except for startDate"""          
            check = False
            print("Please type response as MM/DD/YYYY")
if(__name__) == "__main__":
    add_event2()

def add_toDo2():

    client = MongoClient('mongodb://localhost:27017')
    db = client.project0
    col = db['toDo02']

    entryData = {}
    while (True):
        print("_____________________________________")
        toDoName = input("Enter your Enter your To Do Item's name: ")
        print('Saved To Do Item ' + toDoName)
        entryData["toDoName"] = toDoName

        dueDate = input("When is this due? /n ex MM/DD/YYYY: ") 
        format = '%m/%d/%Y'
        check = True
        try:
            check = bool(datetime.strptime(dueDate, format))
            entryData["dueDate"] = dueDate
            weekDay = datetime.strptime(dueDate,"%A").date()
            entryData["weekday"] = weekDay
   
        except ValueError:
            """Except for dueDate"""          
            check = False
            print("Please type response as MM/DD/YYYY")
        print(entryData)
    
        entryData_id = col.insert_one(entryData).inserted_id
        print({entryData_id})
            
        
if(__name__) == "__main__":
    add_toDo2()



def add_assignment2():

    client = MongoClient('mongodb://localhost:27017')
    db = client.project0
    col = db['assignment02']

    entryData = {}
    while (True):
        print("_____________________________________")
        assignmentName = input("Enter your Enter your Assignment's name: ")
        print('Saved To Do Item ' + assignmentName)
        entryData["assignmentName"] = assignmentName

        dueDate = input("When is this due? /n ex MM/DD/YYYY: ") 
        format = '%m/%d/%Y'
        check = True
        try:
            check = bool(datetime.strptime(dueDate, format))
            entryData["dueDate"] = dueDate
   
        except ValueError:
            """Except for dueDate"""          
            check = False
            print("Please type response as MM/DD/YYYY")
        print(entryData)
        entryData_id = col.insert_one(entryData).inserted_id
        print({entryData_id})            
        
if(__name__) == "__main__":
    add_assignment2()




