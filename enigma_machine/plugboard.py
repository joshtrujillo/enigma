"""
plugboard.py
Class representing the plugboard in the enigma machine.
@author Josh Trujillo
"""


class Plugboard:
    def __init__(self, wiring):
        """
        Initialize plugboard with character mappings.

        Args:
            wiring (str): Plugboard wiring e.g., "AD FV SE".

        Attributes:
            wiring (dict): Dicionary with plug mappings.
                Two key:value pairs for each plug.
        """
        self.wiring = {}
        if wiring:
            plug_list = wiring.split()
            for pair in plug_list:
                if len(pair) != 2 or pair[0] in self.wiring or pair[1] in self.wiring:
                    raise ValueError(f"Invalid or duplicate plugboard pair '{pair}'")
                self.wiring[pair[0]] = pair[1]
                self.wiring[pair[1]] = pair[0]

    def swap(self, letter):
        """
        Swaps the input letter with the plugged letter.

        Args:
            letter (str): The input letter.

        Returns:
            str: If letter is swapped, return value. If not, return the letter.
        """
        return self.wiring.get(letter, letter)
