from flask import Flask, jsonify, request
import os

app = Flask(__name__)

session = {username:"", passsword =""}

@app.route('/api/v1/login',methods=['GET'])
def login():
    response = {'user' : user}
    return jsonify(response)