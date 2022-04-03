from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint
import sys
from colorama import init
from termcolor import colored

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
            #     pprint(x)
            
                for value in x.values():
                    print(value)
                print("__________________________")
        if (result6 == "View Event Schedule"):
            col = db['eventEntry']
            for y in col.aggregate([{'$project' : {"_id": False}}]):
                # pprint(y)
                for value in y.values():
                    print(value)
                print("__________________________")
        if (result6 == "View Assignment List"):
            col = db['assignmentEntry']
            for z in col.aggregate([{'$project' : {"_id": False}}]):
                # pprint(z)
                for value in z.values():
                    print(value)
                print("__________________________")
        if (result6 == "View To Do List"):
            col = db['toDoEntry']
            for a in col.aggregate([{'$project' : {"_id": False}}]):
                # pprint(a)
                for value in a.values():
                    print(value)
                print("__________________________")
        if (result6 == "View Entire Schedule"):
            print(colored("Class Schedule", "red"))
            for b in db.classEntry.aggregate([{'$project' : {"_id": False}}]):
                # pprint(b)
                for value in b.values():
                    print(value)
                    # print("=================")
            print("_____________________________________")
            print(colored("Event Schedule", "red"))
            for c in db.eventEntry.aggregate([{'$project' : {"_id": False}}]):
                # pprint(c)
                for value in c.values():
                    print(value)
            print("_____________________________________")
            print(colored("To Do List" "red"))
            for d in db.toDoEntry.aggregate([{'$project' : {"_id": False}}]):
                # pprint(d)
                for value in d.values():
                    print(value)
            print("_____________________________________")
            print(colored("Assignment List", "red"))
            for e in db.assignmentEntry.aggregate([{'$project' : {"_id": False}}]):
                # pprint(e)
                for value in e.values():
                    print(value)
            
if(__name__) == "__main__":
    view_schedule()