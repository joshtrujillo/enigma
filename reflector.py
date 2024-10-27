'''
reflector.py
Class representing the reflector in the enigma machine
@author Josh Trujillo
'''

class Reflector:
    def __init__(self, reflector_type):
        if reflector_type == "A":
            self.wiring = "EJMZALYXVBWFCRQUONTSPIKHGD"
        elif reflector_type == "B":
            self.wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        else: # reflector C
            self.wiring = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

    '''
    reflect(self, letter)
    returns the shifted letter based on the reflector setting
    '''
    def reflect(self, letter):
        # reflect letter
        return self.wiring[ord(letter) - 65]
