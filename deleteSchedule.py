from msilib.schema import Class
from  pymongo import MongoClient
import pymongo
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint

def delete_schedule():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['agendaEntry']
    
    while (True):
        deleteOptions = AgendaMenu(
            {
                1 : "Delete last Entry"
            }
        )
        deleteOptions.printAgendaMenu()
        result9 = deleteOptions.menuResponse("What are we deleting? ")
        if (result9 == "Delete last Entry"):
            chooseEntry = AgendaMenu(
                {
                    1 : "Class",
                    2 : "Event",
                    3 : "To Do",
                    4 : "Assignment"
                }
            )
            chooseEntry.printAgendaMenu()
            result10 = chooseEntry.menuResponse("From Where? ")
        if (result10 == "Class"):
            # col = db['classEntry']
            docs = db.classEntry.find().sort([("$natural", -1)]).limit(1)
            # docs = db.classEntry.find_one({"_id": -1})
            # docs = db.classEntry.find({}, {$natural: -1})
            # print(docs)
            for p in docs:
                pprint(p)
            col.delete_one(p)  
            print(result9.deleted_count)
        if(result10 == "Event"):
            docs = db.eventEntry.find().sort([("$natural", -1)]).limit(1)
            for q in docs:
                pprint(q)
            col.delete_one(q)  
            print(result9.deleted_count)
        if (result10 == "To Do"):
            docs = db.toDoEntry.find().sort([("$natural", -1)]).limit(1)
            for r in docs:
                pprint(r)
            col.delete_one(r)  
            print(result9.deleted_count)
        if (result10 == "Assignment"):
            docs = db.assignmentEntry.find().sort([("$natural", -1)]).limit(1)
            for s in docs:
                pprint(s)
            col.delete_one(s)  
            print(result9.deleted_count)
if(__name__) == "__main__":
    delete_schedule()
