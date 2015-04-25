__author__ = 'ugur'
import datetime
from pymongo import MongoClient

client= MongoClient('mongodb://ugurcan:123456789@ds029640.mongolab.com:29640/teamred')
db=client.teamred
koleksiyon= db.koleksiyon

post = {"author": "gicik",
        "text": "My fgdfg bilakdfa post!",

       "date": datetime.datetime.utcnow()}
post_id = koleksiyon.insert_one(post).inserted_id
print koleksiyon.find_one()


