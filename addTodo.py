from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint

def create_Todo():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['toDoEntry']

    entryData = {}
    while (True):
        print("_____________________________________")
        toDoName = input("Enter your To do Item's Name: ")
        print('Saved To do Item ' + toDoName)
        entryData["toDoName"] = toDoName
        if (toDoName == ""):
            print('Please enter your Event Name: ')
        
        entryWeekday = AgendaMenu(    
            {
                1 : "Monday",
                2 : "Tuesday",
                3 : "Wednesday",
                4 : "Thursday",
                5 : "Friday",
                6 : "Saturday",
                7 : "Sunday"
                }
            )
        entryWeekday.printAgendaMenu()
        resultWeekday = entryWeekday.menuResponse("Please enter the number corresponding with you to do item's due date ")
        entryData["weekday"] = resultWeekday

        print(entryData)
        entryData_id = col.insert_one(entryData).inserted_id
        print({entryData_id})

if(__name__) == "__main__":
    create_Todo()