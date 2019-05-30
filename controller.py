import redis
import os

def initDB():
    if 'VCAP_SERVICES' in os.environ:
        VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
        CREDENTIALS = VCAP_SERVICES["rediscloud"][0]["credentials"]
        r = redis.Redis(host=CREDENTIALS["hostname"], port=CREDENTIALS["port"], password=CREDENTIALS["password"])
    else:
        r = redis.Redis(host='127.0.0.1', port='6379')

    return r

#Login method take user and password string
def login(uname, pwd):
    print uname
    print pwd
    return True

# Function to acquire User Permissions or Role
# Initial attempt is binary - It is either "Administrator" or a "User" - No other options at this time
def role(uname):
    print uname
    user.getuser(uname)
    return user['role']
