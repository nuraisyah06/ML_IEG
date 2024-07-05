'''
flask is a module
inside this module
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_Hello():
    return "Hello Doonia Tipuw Tipuw!"

