from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint
from addOreditEntry import choose_create
from viewSchedule import view_schedule
from deleteSchedule import delete_schedule

def greeting():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['agendaEntry']

    entryData = {}

    studentName = ""
    print("What's your name/n")
    while (True):
    
        studentName = input('Enter your name: ')
        print('Hello ' + studentName)
        entryData["name"] = studentName
        if (studentName == ""):
            print('Please enter your Name: ')
        
        option = AgendaMenu(
            {
                1 : "View Shcedule",
                2 : "Edit Schedule",
                3 : "Delete Schedule"
                }
            )

        option.printAgendaMenu()
        result = option.menuResponse("Please enter what type of Agenda Entry you are making. ")
        entryData["entryType"] = result
        if (result == "View Shcedule"):
            view_schedule()
        elif (result == "Edit Schedule"):
            choose_create()
        elif (result == "Delete Schedule"):
            delete_schedule()
        break

if(__name__) == "__main__":
    greeting()

# print(client.list_database_names())
# print(db.list_collection_names())


# in case it does not work
# Press CTRL+SHIFT+P
# Enter "Python: Select Interpretor"
# Then select the python.exe that is not not from ananconda.