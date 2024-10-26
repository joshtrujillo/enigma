'''
rotor.py
Class for each rotor in the enigma machine
@author Josh Trujillo
'''

class Rotor:
    def __init__(self, wiring, notch, initial_position=0):
        self.wiring = wiring
        self.notch = notch
        self.position = initial_position

    def rotate(self):
        # rotate and handle the notch turnover
        pass

    def forward_substitute(self, letter):
        # perform forward substitution
        pass

    def backward_substitute(self, letter):
        # perform backward substitution
        pass

