from flask import Flask, request, jsonify
import json, os

AUTHOR = os.environ['AUTHOR'] 

app=Flask(__name__)


@app.route('/', methods=['GET'])
def get_project():
    res = {
        'env': AUTHOR,
        'app': "Python Flask",
        'method': "GET",
        'status': 200
    }
    return jsonify(res)