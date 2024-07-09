'''
flask is a module
inside this module
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_Hello():
    return '''
        <html>
            <head>
                <title> Hello World </title>
            </head>
            <body>
                <h1> Hello World </h1>
                <h2> Hai </h2>
                
                
            </body>
        </html>'''
    

@app.route("/products")
def getProduct():
    return ["apple", "orange", "mango"]