'''
rotor.py
Class for each rotor in the enigma machine
@author Josh Trujillo
'''

class Rotor:
    def __init__(self, rotor, initial_position=0):
        '''
        Args:
            rotor: String for the rotor e.g. "I".
            initial_position: Int for starting position, default is 0.

        Atributes:
            position: Int for the rotor position.
            wiring: String for the rotor substitution.
            notch: Char at the rotor notch.
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
        Rotate the rotor and return true if the
        current position matches the rotor.

        Returns:
            True if the new position is at the notch.
        '''
        self.position += 1 % 26
        return self.position == self.notch

    def forward_substitute(self, letter):
        '''
        Rotor substitution before reaching the reflector.

        Args:
            letter: The input letter.

        Returns:
            Output of the rotor.
        '''
        return self.wiring[(ord(letter) - 65 + self.position) % 26]

    def backward_substitute(self, letter):
        '''
        Rotor substitution after passing the reflector.

        Args:
            letter: The input letter.

        Returns:
            Output of the rotor going backwards.
        '''
        return chr(self.wiring.index(letter) + 65)
