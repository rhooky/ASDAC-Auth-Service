from flask import Flask, jsonify, request
import os
import controller
import model


app = Flask(__name__)


@app.route('/api/v1/authenticate',methods=['GET'])
def auth():
    
    auth = request.args
    response = controller.login(auth['username'], auth['password'])
    
    return jsonify(response)
    code = 202

@app.route('/api/v1/getNotificationMethod',methods=['GET'])
def notify():
    
    user = request.args
    response = controller.getNotificationMethod()
    

    return jsonify(response)
    code = 202

#initiates flask server
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))

    