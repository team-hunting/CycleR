#!/usr/bin/env python3
from flask import Flask, render_template #, request, send_from_directory, send_file

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('cycle.html')

@app.route('/api/scrape', methods=['POST'])
def getCycleData():
    return {}
