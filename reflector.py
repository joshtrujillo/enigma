'''
reflector.py
Class representing the reflector in the enigma machine.
@author Josh Trujillo
'''

class Reflector:
    def __init__(self, reflector_type):
        '''
        Args:
            reflector_type (str): Reflector type e.g., "A" or "B".

        Attributes:
            wiring (str): Reflector wiring.
        '''
        if reflector_type == "A":
            self.wiring = "EJMZALYXVBWFCRQUONTSPIKHGD"
        elif reflector_type == "B":
            self.wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        else: # reflector C
            self.wiring = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

    def reflect(self, letter):
        '''
        Pass letter through reflector wiring.

        Returns:
            str: Reflected letter.
        '''
        return self.wiring[ord(letter) - 65]
