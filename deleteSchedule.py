from msilib.schema import Class
from  pymongo import MongoClient
import pymongo
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint

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
            docs = db.classEntry.find().sort({"_id":-1}).limit(1)
            for p in docs:
                print(p)
            # col.delete_one(p)  
            # print(result9.deleted_count)
if(__name__) == "__main__":
    delete_schedule()
