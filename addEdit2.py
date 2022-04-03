from tracemalloc import start
from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint
import json
# from Project0 import greeting
from addClass import add_class
import sys
import datetime
import calendar

def add_class2():

    client = MongoClient('mongodb://localhost:27017')
    db = client.project0
    col = db['classEntry']

    entryData = {}
    
    print("_____________________________________")
    className = input('Enter your Class Name: ')
    print('Saved class ' + className)
    entryData["className"] = className
    if (className == ""):
        print('Please enter your Class Name: ')
    else:
        startDate = input("What date does this class start? /n ex MM/DD/YYYY: ") 
        resultDate = datetime.datetime.strptime(startDate,"%b/%d/%Y").date()   
        print(" starts " + resultDate.strftime('%a, %b/%d/%Y'))
        entryData["startDate"] = startDate
    
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
    entryData["weekday"] = resultWeekday
           
    classTime = 0
    hhh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    classTime = int(input("Enter the hour your class starts. /n ex, 10 for 10:30: "))
    print(classTime, type(classTime))
    if classTime in hhh:
        print('Saved ')
        entryData["classHour"] = classTime

    classTimeM = 0
    mmm = range(60)
    classTimeM = int(input("Enter the minutes your class starts. /n ex, 30 for 10:30: "))
    print(classTimeM, type(classTimeM))
    if classTimeM in mmm:
        print('Saved ')
        entryData["classMinute"] = classTimeM
        
    # return studentName
    
    print(entryData)
    entryData_id = col.insert_one(entryData).inserted_id
    print({entryData_id})
    
if(__name__) == "__main__":
    add_class()