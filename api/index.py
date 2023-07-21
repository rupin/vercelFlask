from flask import Flask
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!123'


@app.route('/about')
def about():
    return 'About'

@app.route('/incoming')
def incoming():
    print('This is a debug message')
    return "Something Else"