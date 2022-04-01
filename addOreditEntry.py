from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
from pprint import pprint
import json
# from Project0 import greeting
from addAssignment import create_Assignment
from addClass import add_class
from addEvent import create_Event
from addTodo import create_Todo
import sys

"""These are functions to update different entries"""
def class_change():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # dbclassEntry = db['classEntry']
    nameChange = AgendaMenu(
        {
            1 : "Update Class Name",
            2 : "Update Class Hour",
            3 : "Update Class Minute",
            4 : "Update Class Day",
            0 : "Exit"
        }
    )
    nameChange.printAgendaMenu()
    resultName = nameChange.menuResponse("What are we updating? ")
    if (resultName == "Exit"):
           sys.exit()
    if (resultName == "Update Class Name"):
        OriginalclassName = input('Enter the Class name we are changing: ')
        ChangeclassName = input('Enter what we are changing the Class Name to ')
        ocn = {"className" : OriginalclassName}
        ccn = {"$set": {"className" : ChangeclassName}}
        change = db.classEntry.update_many(ocn, ccn)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Class Hour"):
        OriginalclassHour = int(input('Enter the Class hour we are changing. n/ ex: 10 for 10:15: '))
        ChangeclassHour = int(input('Enter what you are changing the Class minute to. n/ ex: 10 for 10:15: '))
        och = {"classHour" : OriginalclassHour}
        cch = {"$set": {"classHour" : ChangeclassHour}}
        change = db.classEntry.update_many(och, cch)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Class Minute"):
        OriginalclassMinute = int(input('Enter the Class minute we are changing. n/ ex: 15 for 10:15: '))
        ChangeclassMinute = int(input('Enter what you are changing the Class minute to. n/ ex: 15 for 10:15: '))
        ocm = {"classHour" : OriginalclassMinute}
        ccm = {"$set": {"classHour" : ChangeclassMinute}}
        change = db.classEntry.update_many(ocm, ccm)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Class Day"):
        OriginalclassDay = input('Enter the Class day we are changing: ')
        entryWeekday = AgendaMenu(    
            {
                1 : "Monday",
                2 : "Tuesday",
                3 : "Wednesday",
                4 : "Thursday",
                5 : "Friday",
                6 : "Saturday"
                }
            )
        entryWeekday.printAgendaMenu()
        ChangeclassDay = entryWeekday.menuResponse('Enter what we are changing the Class Name to ')
        ocd = {"weekday" : OriginalclassDay}
        ccd = {"$set": {"weekday" : ChangeclassDay}}
        change = db.classEntry.update_many(ocd, ccd)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
if(__name__) == "__main__":
    class_change()

def event_change():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # dbclassEntry = db['classEntry']
    nameChange = AgendaMenu(
        {
            1 : "Update Event Name",
            2 : "Update Event Hour",
            3 : "Update Event Minute",
            4 : "Update Event Day",
            0 : "Exit"
        }
    )
    nameChange.printAgendaMenu()
    resultName = nameChange.menuResponse("What are we updating? ")
    if (resultName == "Exit"):
           sys.exit()
    if (resultName == "Update Event Name"):
        OriginaleventName = input('Enter the Event name we are changing: ')
        ChangeeventName = input('Enter what we are changing the Event Name to ')
        oen = {"eventName" : OriginaleventName}
        cen = {"$set": {"eventName" : ChangeeventName}}
        change = db.classEntry.update_many(oen, cen)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Event Hour"):
        OriginaleventHour = int(input('Enter the Event hour we are changing. n/ ex: 10 for 10:15: '))
        ChangeeventHour = int(input('Enter what you are changing the Event minute to. n/ ex: 10 for 10:15: '))
        oeh = {"eventHour" : OriginaleventHour}
        ceh = {"$set": {"eventHour" : ChangeeventHour}}
        change = db.classEntry.update_many(oeh, ceh)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Event Minute"):
        OriginaleventMinute = int(input('Enter the Event minute we are changing. n/ ex: 15 for 10:15: '))
        ChangeeventMinute = int(input('Enter what you are changing the Event minute to. n/ ex: 15 for 10:15: '))
        oem = {"classHour" : OriginaleventMinute}
        cem = {"$set": {"classHour" : ChangeeventMinute}}
        change = db.classEntry.update_many(oem, cem)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Event Day"):
        OriginaleventDay = input('Enter the Event day we are changing: ')
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
        ChangeeventDay = entryWeekday.menuResponse('Enter what we are changing the Class Name to ')
        oed = {"weekday" : OriginaleventDay}
        ced = {"$set": {"weekday" : ChangeeventDay}}
        change = db.classEntry.update_many(oed, ced)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
if(__name__) == "__main__":
    event_change() 

def toDO_change():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # dbclassEntry = db['classEntry']
    nameChange = AgendaMenu(
        {
            1 : "Update To Do Name",
            2 : "Update Due Date",    
            0 : "Exit"
        }
    )
    nameChange.printAgendaMenu()
    resultName = nameChange.menuResponse("What are we updating? ")
    if (resultName == "Exit"):
           sys.exit()
    if (resultName == "Update To Do Name"):
        OriginaltoDoName = input('Enter the To Do name we are changing: ')
        ChangetoDoName = input('Enter what we are changing the To Do Name to ')
        oen = {"eventName" : OriginaltoDoName}
        cen = {"$set": {"eventName" : ChangetoDoName}}
        change = db.classEntry.update_many(oen, cen)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Due date"):
        OriginaltoDoDay = input("Enter the To Do item's due date we are changing: ")
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
        ChangeeventDay = entryWeekday.menuResponse("Enter the To Do item's due date we are changing it to: ")
        oed = {"weekday" : OriginaltoDoDay}
        ced = {"$set": {"weekday" : ChangeeventDay}}
        change = db.eventEntry.update_many(oed, ced)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
if(__name__) == "__main__":
    toDO_change()

def assignment_change():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # dbclassEntry = db['classEntry']
    nameChange = AgendaMenu(
        {
            1 : "Update Assignment Name",
            2 : "Update Due Date",
            3 : "Class Name",
            0 : "Exit"
        }
    )
    nameChange.printAgendaMenu()
    resultName = nameChange.menuResponse("What are we updating? ")
    if (resultName == "Exit"):
           sys.exit()
    if (resultName == "Update Assignment Name"):
        OriginalassignmentName = input('Enter the Assignment name we are changing: ')
        ChangeassignmentName = input('Enter what we are changing the Assignment Name to ')
        oan = {"eventName" : OriginalassignmentName}
        can = {"$set": {"eventName" : ChangeassignmentName}}
        change = db.toDoEntry.update_many(oan, can)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
    if (resultName == "Update Event Day"):
        OriginalassignmentDay = input("Enter the Assignment's due date we are changing: ")
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
        ChangeassignmentDay = entryWeekday.menuResponse("Enter the Assignments's due date we are changing it to: ")
        oad = {"weekday" : OriginalassignmentDay}
        cad = {"$set": {"weekday" : ChangeassignmentDay}}
        change = db.assignmentEntry.update_many(oad, cad)
        print("Entires Changed")
        print(change.modified_count)
        print("__________________________")
if(__name__) == "__main__":
    assignment_change() 


"""These are functions to UPLOAD different entries"""
def upload_class():
    client = MongoClient('mongodb://localhost:27017')
    db = client.project0

    uploadNameC = input("Please type the name of the file you are uploading. n/ ex filename.json: ")
    print("Uploaded Entry(s) into Class Schedule.")
    # col = db['toDoEntry']
    with open (uploadNameC) as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        db.classEntry.insert_many(file_data)
    else:
        db.classEntry.insert_one(file_data)
if(__name__) == "__main__":
    upload_class()     

def upload_event():
    client = MongoClient('mongodb://localhost:27017')
    db = client.project0

    uploadNameE = input("Please type the name of the file you are uploading. n/ ex filename.json: ")
    print("Uploaded Entry(s) into Class Schedule.")
    # col = db['toDoEntry']
    with open (uploadNameE) as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        db.eventEntry.insert_many(file_data)
    else:
        db.eventEntry.insert_one(file_data)
if(__name__) == "__main__":
    upload_event()

def upload_toDo():
    client = MongoClient('mongodb://localhost:27017')
    db = client.project0

    uploadNameTD = input("Please type the name of the file you are uploading. n/ ex filename.json: ")
    print("Uploaded Entry(s) into Class Schedule.")
    # col = db['toDoEntry']
    with open (uploadNameTD) as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        db.toDoEntry.insert_many(file_data)
    else:
        db.toDoEntry.insert_one(file_data)
if(__name__) == "__main__":
    upload_toDo()

def upload_assignment():
    client = MongoClient('mongodb://localhost:27017')
    db = client.project0

    uploadNameA = input("Please type the name of the file you are uploading. n/ ex filename.json: ")
    print("Uploaded Entry(s) into Class Schedule.")
    # col = db['toDoEntry']
    with open (uploadNameA) as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        db.assignmentEntry.insert_many(file_data)
    else:
        db.assignmentEntry.insert_one(file_data)
if(__name__) == "__main__":
    upload_assignment()



"""This is the main function"""
def choose_create():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    # col = db['agendaEntry']

    entryData = {}
    while (True):
        choose = AgendaMenu(
            {
                1 : "Update Entry",
                2 : "Add new Entry",
                3 : "Upload Entry",
                0 : "Exit"
            }
        )
        choose.printAgendaMenu()
        result5 = choose.menuResponse("What would you like to do? ")
        if (result5 == "Exit"):
           sys.exit() 
        if (result5 == "Upload Entry"):
            choose2 = AgendaMenu(
            {
                1 : "Class",
                2 : "Event",
                3 : "To Do",
                4 : "Assignment",
                0 : "Exit"
            })
            choose2.printAgendaMenu()
            resultupload = choose2.menuResponse("What Entry type are we uploading? ")
            if (resultupload == "Exit"):
                sys.exit()
            if (resultupload == "Class"):
                upload_class()
            if (resultupload == "Event"):
                upload_event()
            if (resultupload == "To Do"):
                upload_toDo()
            if (resultupload == "Assignment"):
                upload_assignment()
            # print("Uploaded Entry(s) into To Do list.")
            # # col = db['toDoEntry']
            # with open ('ToDoList.json') as file:
            #     file_data = json.load(file)
            # if isinstance(file_data, list):
            #     db.toDoEntry.insert_many(file_data)
            # else:
            #     db.toDoEntry.insert_one(file_data)
        elif(result5 == "Update Entry"):
            choose2 = AgendaMenu(
            {
                1 : "Class",
                2 : "Event",
                3 : "To Do",
                4 : "Assignment"
            })
            choose2.printAgendaMenu()
            result2 = choose2.menuResponse("What Entry type are we updating ")
            
            if (result2 == "Class"):
                    col = db['classEntry']
                    for x in col.find():
                        pprint(x)
                    print("__________________________")
                    class_change()
            elif (result2 == "Event"):
                col = db['eventEntry']
                for y in col.find():
                    pprint(y)
                print("__________________________")
                event_change()
            elif (result2 == "To Do"):
                col = db['toDoEntry']
                for a in col.find():
                    pprint(a)
                print("__________________________")
                toDO_change()
            elif (result2 == "Assignment"):
                col = db['assignmentEntry']
                for z in col.find():
                    pprint(z)
                print("__________________________")
                assignment_change()
        elif(result5 == "Add new Entry"):           
            choose3 = AgendaMenu(
            {
                1 : "Class",
                2 : "Event",
                3 : "To Do",
                4 : "Assignment"
            })
            choose3.printAgendaMenu()
            result3 = choose3.menuResponse("What Entry type are we adding? ")
            if (result3 == "Class"):
                add_class()
            if (result3 == "Event"):
                create_Event()
            if (result3 == "To Do"):
                create_Todo()
            if (result3 == "Assignment"):
                create_Assignment()

if(__name__) == "__main__":
    choose_create()




