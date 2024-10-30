'''
plugboard.py
Class representing the plugboard in the enigma machine
@author Josh Trujillo
'''

class Plugboard:
    def __init__(self, wiring):
        self.wiring = {}
        for pair in wiring:
            print(pair)
            self.wiring[pair[0]] = pair[1]
            self.wiring[pair[1]] = pair[0]

    def swap(self, letter):
        # swap letter based on plugboard wiring
        if letter in self.wiring:
            return self.wiring[letter]
        else:
            return letter
