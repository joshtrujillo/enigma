'''
rotor.py
Class for each rotor in the enigma machine
@author Josh Trujillo
'''

class Rotor:
    def __init__(self, rotor, initial_position=0):
        '''
        attributes:
        wiring
        notch
        position
        '''
        self.position = initial_position
        if rotor == "I":
            self.wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            self.notch = "Y"
        elif rotor == "II":
            self.wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            self.notch = "M"
        elif rotor == "III":
            self.wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            self.notch = "D"
        elif rotor == "IV":
            self.wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
            self.notch = "R"
        else: # rotor V
            self.wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
            self.notch = "H"

    def rotate(self):
        '''
        rotate the rotor and return true if the
        current position matches the rotor
        '''
        self.position += 1 % 26
        return self.position == self.notch

    def forward_substitute(self, letter):
        '''
        rotor substitution before reaching the reflector
        '''
        return self.wiring[ord(letter) - 65]

    def backward_substitute(self, letter):
        '''
        rotor substitution after passing the reflector
        '''
        return chr(self.wiring.index(letter) + 65)
