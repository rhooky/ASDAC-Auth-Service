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

def login(uname, pwd):
    print uname
    print pwd
    return True