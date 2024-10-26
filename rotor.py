'''
rotor.py
Class for each rotor in the enigma machine
@author Josh Trujillo
'''

class Rotor:
    def __init__(self, rotor, initial_position=0):
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
        # rotate and handle the notch turnover
        pass

    def forward_substitute(self, letter):
        # perform forward substitution
        pass

    def backward_substitute(self, letter):
        # perform backward substitution
        pass

