import controller

r = controller.initDB()

#creates a new user with all attributes
def createUser(username, password, email, phone, role):
    user_key = role + "_" + username
    r.hmset(user_key, {"username" : username, "password" : password, "email" : email, "phone" : str(phone), "role" : role})
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