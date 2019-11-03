#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
import handle

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify(handle.output)      