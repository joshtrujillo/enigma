'''
reflector.py
Class representing the reflector in the enigma machine.
@author Josh Trujillo
'''

class Reflector:
    def __init__(self, reflector_type):
        '''
        Args:
            reflector_type: String for the reflector type e.g. "A".

        Attributes:
            wiring: String reprsenting the reflector wiring.
        '''
        if reflector_type == "A":
            self.wiring = "EJMZALYXVBWFCRQUONTSPIKHGD"
        elif reflector_type == "B":
            self.wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        else: # reflector C
            self.wiring = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

    def reflect(self, letter):
        '''
        Returns the shifted letter based on the reflector setting.
        '''
        return self.wiring[ord(letter) - 65]
