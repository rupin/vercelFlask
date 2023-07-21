from flask import Flask
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/incoming')
def incoming():
    logging.debug('This is a debug message')
    return "Something Else"