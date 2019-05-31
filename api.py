from flask import Flask, jsonify, request
import os
import controller
import model


app = Flask(__name__)


model.deleteUser("tim")
model.deleteUser("bob")
model.deleteUser("berryl")
model.createUser("tim", "password", "tim@email.com", "1234", "admin", "email")
model.createUser("bob", "password", "bob@email.com", "1234", "user", "email")
model.createUser("berryl", "password", "berryl@email.com", "1234", "handler", "phone")


@app.route('/api/v1/authenticate',methods=['GET'])
def auth():
    
    auth = request.args
    response = controller.login(auth['username'], auth['password'])
    code = 200
    return jsonify(response)
    

@app.route('/api/v1/getNotificationMethod',methods=['GET'])
def notify():
    user = request.args['username']
    response = controller.getNotification(user)
    code = 200
    return jsonify(response)
    

@app.route('/api/v1/getPermissions',methods=['GET'])
def perms():
    user = request.args['username']
    response = controller.getRole(user)
    code = 200
    return jsonify(response)
    

@app.route('/api/v1/ping',methods=['GET'])
def ping():
    code = 200
    return "Online"
    

@app.route('/api/v1/FilterFieldsByUser',methods=['GET'])
def fields():
    user = request.args['username']
    role = controller.getRole(user)
    
    if role == 'admin':
        response = "EDIT, UPDATE, DELETE, CREATE, VIEW"
    if role == 'user':
        response = "VIEW"
    if role == 'handler':
        response = "VIEW, UPDATE"
    
    code = 200
    return jsonify(response)
    


#initiates flask server
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))

    