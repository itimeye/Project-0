class AgendaMenu:
    def __init__(self, menu: dict):
        self.menu = menu
    
    def printAgendaMenu(self):
        for i in self.menu:
            print(f"{i}. {self.menu[i]}")
        # print("0. Exit")

    def menuResponse(self, feedback):
        while True:
            try:
                self.entry = int(input(f"{feedback}"))
                if self.entry <= len(self.menu): #and self.entry >= 0:
                    return self.menu[self.entry]
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

# Weekday_Type = AgendaMenu(
#     {
#         1 : "Monday",
#         2 : "Tuesday",
#         3 : "Wednesday",
#         4 : "Thursday",
#         5 : "Friday",
#         6 : "Saturday"
#     }
# )

# Minute_Type = AgendaMenu(
#     {
#         1 : "00",
#         2 : "15",
#         3 : "30",
#         4 : "45"
#     }
# )