from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint
import sys

def view_schedule():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # col = db['agendaEntry']

    # entryData = {}
    while (True):
        optionA = AgendaMenu( 
        {
            1 : "View Class Schedule",
            2 : "View Event Schedule",
            3 : "View To Do List",
            4 : "View Assignment List",
            5 : "View Entire Schedule",
            0 : "Exit"
        }
        )
        optionA.printAgendaMenu()
        result6 = optionA.menuResponse("What would you like to do? ")
        if (result6 == "Exit"):
           sys.exit()
        if (result6 == "View Class Schedule"):
            col = db['classEntry']
            for x in col.aggregate([{'$project' : {"_id": False}}]):
                pprint(x)
                print("__________________________")
        if (result6 == "View Event Schedule"):
            col = db['eventEntry']
            for y in col.aggregate([{'$project' : {"_id": False}}]):
                pprint(y)
                print("__________________________")
        if (result6 == "View Assignment List"):
            col = db['assignmentEntry']
            for z in col.aggregate([{'$project' : {"_id": False}}]):
                pprint(z)
                print("__________________________")
        if (result6 == "View To Do List"):
            col = db['toDoEntry']
            for a in col.aggregate([{'$project' : {"_id": False}}]):
                pprint(a)
                print("__________________________")
        if (result6 == "View Entire Schedule"):
            print("Class Schedule")
            for b in db.classEntry.aggregate([{'$project' : {"_id": False}}]):
                pprint(b)
            print("_____________________________________")
            print("Event Schedule")
            for c in db.eventEntry.aggregate([{'$project' : {"_id": False}}]):
                pprint(c)
            print("_____________________________________")
            print("To Do List")
            for d in db.toDoEntry.aggregate([{'$project' : {"_id": False}}]):
                pprint(d)
            print("_____________________________________")
            print("Assignment List")
            for e in db.assignmentEntry.aggregate([{'$project' : {"_id": False}}]):
                pprint(e)
            
if(__name__) == "__main__":
    view_schedule()