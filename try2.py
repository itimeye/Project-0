from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint
from addOreditEntry import choose_create

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
        # entryData["entryType"] = result
        if (result == "View Shcedule"):
            view_Schedule()
        elif (result == "Edit Schedule"):
            choose_create()
        elif (result == "Delete Schedule"):
            delete_Schedule()
        break

    
    
    
if(__name__) == "__main__":
    greeting()


def view_Schedule():
    print("this is function View Schedule")

def edit_Schedule():
    print("this is function edit Schedule")

def delete_Schedule():
    print("this is function delete Schedule")