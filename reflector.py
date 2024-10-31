"""
reflector.py
Class representing the reflector in the enigma machine.
@author Josh Trujillo
"""


class Reflector:
    def __init__(self, reflector_type):
        """
        Initialize the reflector with a specific wiring based on the type

        Args:
            reflector_type (str): Reflector type e.g., "A" or "B".

        Attributes:
            wiring (str): Reflector wiring.
        Raises:
            ValueError: If an invalid reflector type is specified.
        """
        reflectors = {
            "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
            "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
        }
        if reflector_type not in reflectors:
            raise ValueError(
                f"Invalid reflector type '{reflector_type}' \
            Choose 'A', 'B', or 'C'."
            )
        self.wiring = reflectors[reflector_type]

    def reflect(self, letter):
        """
        Pass letter through reflector wiring.

        Args:
            letter (str): The letter to be reflected.

        Returns:
            str: Reflected letter.
        """
        return self.wiring[ord(letter) - ord("A")]
