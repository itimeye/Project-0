# import datetime 
from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint 
# birthday=input("What is your B'day? (in DD/MM/YYYY) ")  
# birthdate=datetime.datetime.strptime(birthday,"%d/%m/%Y").date()  
# print("Your B'day is : "+birthdate.strftime('%d/%B/%Y'))  

# while choice != 'q':
#     # Give all the choices in a series of print statements.
#     print("\n[M] Enter M for Monday")
#     print("[T] Enter T for Tuesday")
#     print("[W] Enter W for Wednesday.")
#     print("[TH] Enter TH for Thursday.")
#     print("[F] Enter F for Thursday.")
#     print("[S] Enter S for Thursday.")


# def class_createB():
#     classTime = ""
#     while (True):
    
#         classTime = int(input("Enter the hour your class starts. /n ex, 10 for 10:30 "))
#         print('Saved ' + str(classTime))
#         if(classTime >= 1): 
#             print('Error')
#         elif(classTime <= 12):
#             print('Error')
#         else:
#             break
    
#     return classTime

# class_createB()
# print(class_createB())

# def class_createB():
#     classTime = 1
#     while classTime in range(1,13):
    
#         classTime = int(input("Enter the hour your class starts. /n ex, 10 for 10:30 "))
#         print('Saved')
#         if(classTime >= 1): 
#             print('Error')
#         elif(classTime <= 12):
#             print('Error')
#         else:
#             break
    
#     return classTime

# class_createB()
# print(class_createB())

# def class_createC():
#     classTimeM = ""
#     while (True):
    
#         classTimeM = int(input("Enter the hour your class starts. /n ex, 10 for 10:30 "))
#         print('Saved ' + str(classTimeM))
#         if(classTimeM >= 0): 
#             print('Error')
#         elif(classTimeM <= 59):
#             print('Error')
#         else:
#             break
    
#     return classTimeM

# class_createC()
# print(class_createC())

# def class_createD():
#     classTeacher = ""
#     while (True):
    
#         classTeacher = input("Enter your Teacher's Name: ")
#         print('Saved class ' + classTeacher)
#         if (classTeacher == ""):
#             print('Please enter your Class Name: ')
#         else:
#             break
    
#     return classTeacher

# p= class_createD
# print(p)

# def class_createC():
#     classTimeM = 0
#     mmm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     while (True):
        
#         classTimeM = int(input("Enter the hour your class starts. /n ex, 10 for 10:30:"))
#         print(classTimeM, type(classTimeM))
#         if classTimeM in mmm:
#             print('Saved ')
#             break

#     return classTimeM

# class_createC()

# from calendar import week
# from MenuClass import AgendaMenu


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
        # return studentName 
        else:
            option = AgendaMenu(
                {
                    1 : "View Schedule",
                    2 : "Add to Schedule",
                    3 : "Delete Schedule"
                }
            )
        option.printAgendaMenu()
        result = option.menuResponse("What are you doing today? ")
        entryData["entryType"] = result
        break
    
if(__name__) == "__main__":
    greeting()
    
# def Add_to_Schedule():
#     client = MongoClient('mongodb://localhost:27017')
#     db = client.project0
#     col = db['agendaEntry']

#     entryData = {}
    
#     entry = AgendaMenu(
#             {
#             1 : "Class",
#             2 : "Event",
#             3 : "To Do",
#             4 : "Assignment"
#             }
#     )

#     entry.printAgendaMenu()
#     result = entry.menuResponse("Please enter what type of Agenda Entry you are making. ")
#     entryData["entryType"] = result
    
    
#     if (result == "Class"):
#         className = input('Enter your Class Name: ')
#         print('Saved class ' + className)
#         entryData["className"] = className
#         if (className == ""):
#             print('Please enter your Class Name: ')
        
#         entryWeekday = AgendaMenu(    
#             {
#                 1 : "Monday",
#                 2 : "Tuesday",
#                 3 : "Wednesday",
#                 4 : "Thursday",
#                 5 : "Friday",
#                 6 : "Friday"
#                 }
#             )
#         entryWeekday.printAgendaMenu()
#         resultWeekday = entryWeekday.menuResponse("Please enter what type of Agenda Entry you are making. ")
#         entryData["weekday"] = resultWeekday
           
#     classTime = 0
#     hhh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     classTime = int(input("Enter the hour your class starts. /n ex, 10 for 10:30: "))
#     print(classTime, type(classTime))
#     if classTime in hhh:
#         print('Saved ')
#         entryData["classHour"] = classTime

#     classTimeM = 0
#     mmm = range(60)
#     classTimeM = int(input("Enter the minutes your class starts. /n ex, 30 for 10:30: "))
#     print(classTimeM, type(classTimeM))
#     if classTimeM in mmm:
#         print('Saved ')
#         entryData["classMinute"] = classTimeM
        
#     # return studentName
    
#     print(entryData)
#     # entryData_id = col.insert_one(entryData).inserted_id
#     # print({entryData_id})
    
#     if (result == "Event"):
#         eventName = input('Enter your Event Name: ')
#         print('Saved Event ' + eventName)
#         entryData["entryType"] = result
#         if (className == ""):
#             print('Please enter your Class Name: ')
        
#         entryWeekday = AgendaMenu
#         entryWeekday.printAgendaMenu()
#         resultWeekday = entryWeekday.menuResponse("Please enter what type of Agenda Entry you are making. ")
#         entryData["weekday"] = resultWeekday
# if(__name__) == "__main__":
#     greeting()