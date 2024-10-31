"""
server.py
Webserver for Enigma python project
@author Josh Trujillo
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! How are you doing today?</p>"
