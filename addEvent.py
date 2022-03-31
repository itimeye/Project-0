from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint

def create_Event():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['eventEntry']

    entryData = {}

    while (True):
        print("_____________________________________")
        eventName = input('Enter your Event Name: ')
        print('Saved event ' + eventName)
        entryData["eventName"] = eventName
        if (eventName == ""):
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
        resultWeekday = entryWeekday.menuResponse("Please enter the number corresponding with you events date ")
        entryData["weekday"] = resultWeekday
           
        eventTime = 0
        hhh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        eventTime = int(input("Enter the hour your class starts. /n ex, 10 for 10:30: "))
        print(eventTime, type(eventTime))
        if eventTime in hhh:
            print('Saved ')
            entryData["eventHour"] = eventTime

        eventTimeM = 0
        mmm = range(60)
        eventTimeM = int(input("Enter the minutes your class starts. /n ex, 30 for 10:30: "))
        print(eventTimeM, type(eventTimeM))
        if eventTimeM in mmm:
            print('Saved ')
            entryData["eventMinute"] = eventTimeM
            
        # return studentName
        
        print(entryData)
        entryData_id = col.insert_one(entryData).inserted_id
        print({entryData_id})

if(__name__) == "__main__":
    create_Event()