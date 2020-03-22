from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

    
#AFTER THAT YOU SHOULD RUN:
#1- set FLASK_APP = application.py
#2- flask run


@app.route("/david")
def david():
    return "Hello, David!"
    
@app.route("/<string:name>")
def hi (name):
    res= ("Hello "+ name)
    return res

@app.route("/index")
def index_function():
    return render_template('hello.html')