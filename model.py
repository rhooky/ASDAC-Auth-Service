import os
import pymongo
from pymongo import MongoClient

#connects to PCF linked DB else tries to connect to localhost

global DB_NAME

def initDB():

    if 'VCAP_SERVICES' in os.environ:
        VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
        #CREDENTIALS = VCAP_SERVICES["rediscloud"][0]["credentials"]
        #r = redis.Redis(host=CREDENTIALS["hostname"], port=CREDENTIALS["port"], password=CREDENTIALS["password"])
        MONCRED = VCAP_SERVICES["mlab"][0]["credentials"]
        client = MongoClient(MONCRED["uri"])
        DB_NAME = str(MONCRED["uri"].split("/")[-1])
    else:
        #r = redis.Redis(host='127.0.0.1', port='6379')
        client = MongoClient('127.0.0.1:27017')
        DB_NAME = "auth"
    
    db = client[DB_NAME]
    return db

db = initDB()

#creates a new user with all attributes
def createUser(username, password, email, phone, role, notify):
    db.auth.insert_one({"username" : username, "password" : password, "email" : email, "phone" : str(phone), "notification" : notify, "role" : role})
    #needs error checking to prevent duplicate ID
    user = db.auth.find_one({"username": username})
    return user         

#updates a single key pair for a user
def updateUser(username, key, pair):
    user = returnUser(username)
    db.auth.update_one(
        {"username": username} ,
        {"$set" : {str(key) : pair}}
        )

    return returnUser(username)

def deleteUser(username):
    user = db.auth.delete_many({"username" : username})
    return user

def returnUser(username):
    cursor = db.auth.find({"username": username})
    user = {}
    for eachUser in cursor:
        user = eachUser
    return user