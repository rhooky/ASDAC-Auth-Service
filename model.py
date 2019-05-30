import controller

r = controller.initDB()

def createUser(username, password, email, phone, role):
    user_key = role + "_" + username
    r.hmset(user_key, {"username" : username, "password" : password, "email" : email, "phone" : str(phone), "role" : role})
    user = r.hgetall(user_key)
    return user