'''
enigma.py
enigma machine simulator
@author Josh Trujillo
'''

from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        sefl.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def encrypt_letter(self, letter):
        # encrypt a single letter
        pass

    def encrypt_message(self, message):
        # encrypt a message letter by letter
        pass
