import pymongo
from datetime import datetime
import sys

# python -m pip install pymongo dnspython

def write_to_db(title, date, location, auth):
    client = pymongo.MongoClient("mongodb+srv://{}:{}@skarcluster-zb6ru.gcp.mongodb.net/events".format(auth[0], auth[1]))
    db = client.events
    event = {
        "title": title,
        "date": date,
        "location": location,
    }
    db.events.insert_one(event)

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    write_to_db("test event", datetime(2009, 11, 12, 12), "elsewhere", (username, password))