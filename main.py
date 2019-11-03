#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
# Import module that handles message classification for all messages from API
import handle

# Setting up Flask
app = Flask(__name__)
CORS(app)

# Serving data in json format via Flask API
@app.route('/')
def index():
    return jsonify(handle.output)

# Set local environment if in use
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) 