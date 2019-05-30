import redis
import os
import model

#Login method take user and password string
def login(uname, pwd):
    print uname
    print pwd
    return True

# Function to acquire User Permissions or Role
# Initial attempt is binary - It is either "Administrator" or a "User" - No other options at this time
def role(uname):
    print uname
    user= getUser(uname)
    return user['role']

def getUser(id):
    return model.returnUser(id)

def getNotification(id):
    user = getUser(id)
    return user['notification']