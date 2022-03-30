from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint

def create_Event():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['agendaEntry']

    entryData = {}

    while (True):
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
                6 : "Friday"
                }
            )
        entryWeekday.printAgendaMenu()
        resultWeekday = entryWeekday.menuResponse("Please enter the number corresponding with you events date ")
        entryData["weekday"] = resultWeekday
           
        classTime = 0
        hhh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        classTime = int(input("Enter the hour your class starts. /n ex, 10 for 10:30: "))
        print(classTime, type(classTime))
        if classTime in hhh:
            print('Saved ')
            entryData["classHour"] = classTime

        classTimeM = 0
        mmm = range(60)
        classTimeM = int(input("Enter the minutes your class starts. /n ex, 30 for 10:30: "))
        print(classTimeM, type(classTimeM))
        if classTimeM in mmm:
            print('Saved ')
            entryData["classMinute"] = classTimeM
            
        # return studentName
        
        print(entryData)
        entryData_id = col.insert_one(entryData).inserted_id
        print({entryData_id})

if(__name__) == "__main__":
    create_Event()