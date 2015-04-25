__author__ = 'ugur'
from pymongo import MongoClient

client= MongoClient('mongodb://ugurcan:123456789@ds029640.mongolab.com:29640/teamred')
db=client.teamred
users=db.users
websites=db.websites
entity=db.entity
