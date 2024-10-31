'''
rotor.py
Class for each rotor in the enigma machine
@author Josh Trujillo
'''

class Rotor:
    def __init__(self, rotor, initial_position=0):
        '''
        Initilize a specific rotor with a position.
            
        Args:
            rotor (str): Rotor representation e.g., "I".
            initial_position (int): Int for starting position, default is 0.

        Atributes:
            position (int): Rotor position.
            wiring (str): Rotor substitution wiring.
            notch (str): Rotor notch.
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
            bool: True if the new position is at the notch.
        '''
        self.position = (self.position + 1) % 26
        return self.position == ord(self.notch) - 65

    def forward_substitute(self, letter):
        '''
        Rotor substitution before reaching the reflector.

        Args:
            letter (str): The input letter.

        Returns:
            str: Output of the rotor.
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
        return chr((self.wiring.index(letter) - self.position + 26) % 26 + 65)
