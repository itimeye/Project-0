from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint


def create_Assignment():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['assignmentEntry']

    entryData = {}

    while (True):
        print("_____________________________________")
        assignmentName = input('Enter your Assignment Name: ')
        print('Saved assignment ' + assignmentName)
        entryData["assignemntName"] = assignmentName
        if (assignmentName == ""):
            print('Please enter your Assignment Name: ')
        
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
        resultWeekday = entryWeekday.menuResponse("Please enter the number corresponding with you assignemnt due date ")
        entryData["weekday"] = resultWeekday
        className = input('Enter the class this assingment is for: ')
        print('Saved class ' + className)
        entryData["className"] = className
        if (className == ""):
            print('Please enter your Class Name: ')
    
        print(entryData)
        entryData_id = col.insert_one(entryData).inserted_id
        print({entryData_id})

if(__name__) == "__main__":
    create_Assignment()