"""
server.py
Webserver for Enigma python project
@author Josh Trujillo
"""

from flask import Flask, render_template, request, redirect, url_for
from enigma_machine import EnigmaMachine, Rotor, Reflector, Plugboard

app = Flask(__name__)


# Homepage route
@app.route("/")
def index():
    return render_template("index.html")


# Encrypt route
@app.route("/encrypt", methods=["POST"])
def encrypt():
    message = request.form["message"]
    rotors = [request.form["rotor1"], request.form["rotor2"], request.form["rotor3"]]
    positions = [
        int(request.form["position1"]),
        int(request.form["position2"]),
        int(request.form["position3"]),
    ]
    reflector = request.form["reflector"]
    plugboard = request.form["plugboard"]

    enigma = EnigmaMachine(rotors, positions, reflector, plugboard)
    ciphertext = enigma.encrypt_message(message)
    return render_template("result.html", result=ciphertext)
