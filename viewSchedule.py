from  pymongo import MongoClient
#from Classoutline import AgendaMenu
from MenuClass import AgendaMenu
import pprint

def view_schedule():
    client = MongoClient('mongodb://localhost:27017')

    db = client.project0
    col = db['agendaEntry']

    entryData = {}
    viewsch = db.collection.aggregate(
        [{
        "$group" :
        {"_id" : "entryType",
        "num_agendaEntry" : {"$sum" : 1}}
        }
    ])
    for i in viewsch:
        print(i)
if(__name__) == "__main__":
    view_schedule()