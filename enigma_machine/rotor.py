"""
rotor.py
Class for each rotor in the enigma machine
@author Josh Trujillo
"""


class Rotor:
    ALPHABET_LENGTH = 26

    def __init__(self, rotor, initial_position=0):
        """
        Initilize a specific rotor with a position.

        Args:
            rotor (str): Rotor representation e.g., "I".
            initial_position (int): Int for starting position, default is 0.

        Atributes:
            position (int): Rotor position.
            wiring (str): Rotor substitution wiring.
            notch (str): Rotor notch.
        """
        self.position = initial_position
        rotor_configs = {
            "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Y"),
            "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "M"),
            "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "D"),
            "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "R"),
            "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", "H"),
        }

        if rotor in rotor_configs:
            self.wiring, self.notch = rotor_configs[rotor]
        else:
            raise ValueError(
                f"Invalid rotor type '{rotor}'. \
                Choose from: {', '.join(rotor_configs.keys())}"
            )

    def rotate(self):
        """
        Rotate the rotor and return true if the
        current position matches the rotor.

        Returns:
            bool: True if the new position is at the notch.
        """
        self.position = (self.position + 1) % Rotor.ALPHABET_LENGTH
        return self.position == ord(self.notch) - ord("A")

    def forward_substitute(self, letter):
        """
        Rotor substitution before reaching the reflector.

        Args:
            letter (str): The input letter.

        Returns:
            str: Output of the rotor.
        """
        return self.wiring[
            (ord(letter) - ord("A") + self.position) % Rotor.ALPHABET_LENGTH
        ]

    def backward_substitute(self, letter):
        """
        Rotor substitution after passing the reflector.

        Args:
            letter (str): The input letter.

        Returns:
            str: Output of the rotor going backwards.
        """
        return chr(
            (self.wiring.index(letter) - self.position + Rotor.ALPHABET_LENGTH)
            % Rotor.ALPHABET_LENGTH
            + ord("A")
        )
