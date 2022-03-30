from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint

def delete_schedule():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['agendaEntry']
    
    while (True):
        deleteOptions = AgendaMenu(
            {
                1 : "Delete last Entry"
            }
        )
        deleteOptions.printAgendaMenu()
        result9 = deleteOptions.menuResponse("What are we deleting? ")
        if (result9 == "Delete last Entry"):
            p = col.find().sort({"_id":-1})
            col.delete_one(p)
            print(result9.deleted_count)
if(__name__) == "__main__":
    delete_schedule()
