from flask import Flask, jsonify, request
import os
from controller.py import *


app = Flask(__name__)



@app.route('/api/v1/authenticate',methods=['GET'])
def auth():
    response = {'status' : 'Up and running'}
    return jsonify(response)
    code = 202


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
    