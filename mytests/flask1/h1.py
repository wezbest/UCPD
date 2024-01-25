'''
Testing the flask app for the first time
'''

# import flask
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
<p>Hello, World!</p>
Sucking and fucking
"""
