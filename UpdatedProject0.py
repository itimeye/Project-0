from cgitb import reset
from tracemalloc import start
from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint
import json
# from Project0 import greeting
import sys
from datetime import datetime
import calendar
from colorama import init
from termcolor import colored 
import addEdit2
from tabulate import tabulate

def gretting():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # col = db['agendaEntry']

    entryData = {}

    studentName = ""
    print("What's your name/n")
    while (True):
    
        studentName = input('Enter your name: ')
        print('Hello ' + studentName)
        entryData["name"] = studentName
        if (studentName == ""):
            print('Please enter your Name: ')

        today = datetime.today()
        print("Today is " + today.strftime("%A, %B %d %Y"))
        print("This is Today's schedule")
        for a in db.assignment02.aggregate([{'$project' : {"assignmentName": True, "dueDate" : True }}]):
                for value in a.values():
                    print(value)
        for t in db.toDoName.aggregate([{'$project' : {"toDoName": True, "dueDate" : True}}]):
                for value in t.values():
                    print(value)
        for c in db.class02.aggregate([{'$project' : {"className": True, "classTime": True}}]):
                for value in c.values():
                    print(value)
        for e in db.event02.aggregate([{'$project' : {"className": True, "classTime": True}}]):
                for value in e.values():
                    print(value) 
        schedule = e, c
        sort_schedule = sorted(schedule.items(), key=lambda x:x[1])

        table = [["Assignment", a]["Task", t]]
        tableSchedule = [[e, c]]
        for i in range(1):
            rowIDs = i
        showindex=rowIDs
        print(tabulate(table, headers="firstrow"))
        print(tabulate(tableSchedule, showindex= rowIDs))

if(__name__) == "__main__":
    gretting()