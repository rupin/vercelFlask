from flask import Flask, request
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!123'


@app.route('/about')
def about():
    return 'About'

@app.route('/incoming', methods = ['GET', 'POST'])
def incoming():
    print('This is a debug message')
    From = request.form["From"]
    print("From: %s" % From)
    return "Hello!"