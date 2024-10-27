'''
plugboard.py
Class representing the plugboard in the enigma machine
@author Josh Trujillo
'''

class Plugboard:
    def __init__(self, wiring):
        self.wiring = wiring

    def swap(self, letter):
        # swap letter based on plugboard wiring
        if letter in self.wiring:
            return self.wiring(letter)
        else:
            return letter
