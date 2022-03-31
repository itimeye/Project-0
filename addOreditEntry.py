from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint
import json
from addAssignment import create_Assignment
from addClass import add_class
from addEvent import create_Event
from addTodo import create_Todo
# from Project0 import greeting

def class_change():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    nameChange = AgendaMenu(
        {
            1 : "Update Class Name",
            2 : "Update Class Hour",
            3 : "Update Class Minute",
            4 : "Update Class Day"
        }
    )
    nameChange.printAgendaMenu()
    resultName = nameChange.menuResponse("What are we updating? ")
    if (resultName == "Update Class Name"):
        OriginalclassName = input('Enter the Class name we are changing: ')
        ChangeclassName = input('Enter what we are changing the Class Name to ')
        ocn = {"className" : {OriginalclassName}}
        ccn = {"$set": {"className" : {ChangeclassName}}}
        change = db.classEntry.update_many(ocn, ccn)
if(__name__) == "__main__":
    class_change()

def choose_create():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # col = db['agendaEntry']

    entryData = {}
    while (True):
        choose = AgendaMenu(
            {
                1 : "Update Entry",
                2 : "Add new Entry",
                3 : "Upload Entry"
            }
        )
        choose.printAgendaMenu()
        result5 = choose.menuResponse("What would you like to do? ")
        # if (result5 == "Exit"):
        #     greeting()
        if (result5 == "Upload Entry"):
            print("Uploaded Entry(s) into To Do list.")
            # col = db['toDoEntry']
            with open ('ToDoList.json') as file:
                file_data = json.load(file)
            if isinstance(file_data, list):
                db.toDoEntry.insert_many(file_data)
            else:
                db.toDoEntry.insert_one(file_data)
        elif(result5 == "Update Entry"):
            choose2 = AgendaMenu(
            {
                1 : "Class",
                2 : "Event",
                3 : "To Do",
                4 : "Assignment"
            })
            choose2.printAgendaMenu()
            result2 = choose2.menuResponse("What Entry type are we updating ")
            
            if (result2 == "Class"):
                    col = db['classEntry']
                    for x in col.find():
                        pprint(x)
                    print("__________________________")
                    class_change()
            elif (result2 == "Event"):
                col = db['eventEntry']
                for y in col.find():
                    pprint(y)
                print("__________________________")
            elif (result2 == "To Do"):
                col = db['toDoEntry']
                for a in col.find():
                    pprint(a)
                print("__________________________")
            elif (result2 == "Assignment"):
                col = db['assignmentEntry']
                for z in col.find():
                    pprint(z)
                print("__________________________")
        elif(result5 == "Add new Entry"):           
            choose3 = AgendaMenu(
            {
                1 : "Class",
                2 : "Event",
                3 : "To Do",
                4 : "Assignment"
            })
            choose3.printAgendaMenu()
            result3 = choose3.menuResponse("What Entry type are we adding? ")
            if (result3 == "Class"):
                add_class()
            if (result3 == "Event"):
                create_Event()
            if (result3 == "To Do"):
                create_Todo()
            if (result3 == "Assignment"):
                create_Assignment()

if(__name__) == "__main__":
    choose_create()




