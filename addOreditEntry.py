from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint
import json

def choose_create():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['agendaEntry']

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
        if (result5 == "Upload Entry"):
            print("Uploaded Entry")
            with open ('ToDoList.json') as file:
                file_data = json.load(file)
            if isinstance(file_data, list):
                col.insert_many(file_data)
            else:
                col.insert_one(file_data)
        try:
            if (result5 == "Update Entry"):
                choose2 = AgendaMenu(
                {
                    1 : "Class",
                    2 : "Event",
                    3 : "To Do",
                    4 : "Assignment"
                }
            )
            choose2.printAgendaMenu()
            result2 = choose2.menuResponse("What Entry type are we updating ")
            
            if (result2 == "Class"):
                    for x in col.find({"className" : ""}):
                        print(x)
            elif (result2 == "Event"):
                    # for y in col.find({"eventName" : ""}):
                        print(y)
            elif (result2 == "To Do"):
                    for z in col.find({"toDoName" : ""}):
                        print(z)
            elif (result2 == "Assignment"):
                    for a in col.find({"assignmentName" : ""}):
                        print(a)
        
        except (result5 == "Add new Entry"):
            choose2
            choose2.printAgendaMenu()
            result2 = choose2.menuResponse("What Entry type are we updating ")

if(__name__) == "__main__":
    choose_create()


