import os
import redis

#connects to PCF linked DB else tries to connect to localhost

def initDB():
    if 'VCAP_SERVICES' in os.environ:
        VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
        CREDENTIALS = VCAP_SERVICES["rediscloud"][0]["credentials"]
        r = redis.Redis(host=CREDENTIALS["hostname"], port=CREDENTIALS["port"], password=CREDENTIALS["password"])
    else:
        r = redis.Redis(host='127.0.0.1', port='6379')

    return r

r = initDB()

#creates a new user with all attributes
def createUser(username, password, email, phone, role, notify):
    user_key = role + "_" + username
    r.hmset(user_key, {"username" : username, "password" : password, "email" : email, "phone" : str(phone), "notification" : notify, "role" : role})
    user = r.hgetall(user_key)
    return user

#updates a single key pair for a user
def updateUser(user_key, key, pair):
    r.hset(user_key, key, pair)
    user = r.hgetall(user_key)
    return user

def deleteUser(user_key):
    user = r.delete(user_key)
    print user
    return user

def returnUser(id):
    user = r.hgetall(id)
    return user