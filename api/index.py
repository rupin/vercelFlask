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
    mediaLength = request.form["NumMedia"]
    print(mediaLength)
    if(int(mediaLength)>0):
        print(request.form["MediaContentType"])

    
    return "Hello!"