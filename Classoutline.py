import datetime
from msilib.schema import Class
from multiprocessing import Event
from urllib import response

# class toDo:
#     '''Base Class for To Do lists
#     '''
#     descriptions = []
#     checklists = {}

#     def __init__(self, descriptions):
#         if descriptions:
#             self.descriptions = descriptions.copy()
#             i = 1
#             for description in descriptions:
#                 self.checklists[i] = description
#                 i += 1
#         else:
#             raise Exception("Please enter a description.")

#     def __str__(self):
#         s = "Here's today's To Do list: \n"
#         for key,value in self.checklists.items():
#             s+= f"- {key} : {value} \n"
#         return s

    # def __init__(self, dueDate, ID):
    #     self.dueDate = dueDate
    #     self.ID = ID

# class toDo(somethingDone):
#     def __init__(self, dueDate, ID, Descrip):
#         super().__init__(dueDate, ID)
#         self.Description = Descrip

# class assignment:
#     names = []
#     datesDue = {}
    
#     def __init__(self, names):
#         if names:
#             self.names = names.copy()
#             i = 1
#             for name in names:
#                 self.datesDue[i] = name
#                 i += 1
#         else:
#             raise Exception("Please enter an Assinment Name.")

#     def __str__(self):
#         s = "Here are your Assignments: \n"
#         for key,value in self.datesDue.items():
#             s+= f"- {key} : {value} \n"
#         return s
    # def __init__(self, dueDate, ID, classFor):
    #     super().__init__(dueDate, ID)
    #     self.forClass = classFor

# class somethingDo:
#     '''Parent class for event and class go
#     '''
#     def __init__(self, dateHeld, ID, name):
#         self.attend = dateHeld
#         self.IDdo = ID
#         self.title = name

# class event(somethingDo):
#     def __init__(self, dateHeld, ID, name, withWho):
#         super().__init__(self, dateHeld, ID, name)
#         self.participant = withWho

# class classGo(somethingDo):
#     def __init__(self, dateHeld, ID, name, Teacher):
#         super().__init__(self, dateHeld, ID, name)
#         self.educator = Teacher


# x = toDo(["wash dishes", "wash dog", "wash hair," "cook lunch for the week"])
# print(x)

# t = assignment(['Project0', 'Color in the lines', 'Take Home Test 12'])
# print(t)

class AgendaMenu:
    def __init__(self, menu: dict):
        self.menu = menu
    
    def printAgendaMenu(self):
        for i in self.menu:
            print(f"{i}. {self.menu[i]}")
        print("0. Exit")

    def menuResponse(self, feedback):
        while True:
            try:
                self.entry = int(input(f"{feedback}"))
                if self.entry <= len(self.menu) and self.entry >= 0:
                    return self.entry
                else:
                    print("That is not an accepted answer. Try again: ")
            except:
                print("Only number values are accepted for Menus. Try again: ")

# Agenda_Type = AgendaMenu(
#     {
#         1 : "Class",
#         2 : "Event",
#         3 : "To Do",
#         4 : "Assignment"
#     }
# )

# Agenda_Type.printAgendaMenu()
# Agenda_Type.menuResponse('Please select your Agenda entry Type ')