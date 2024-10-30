'''
plugboard.py
Class representing the plugboard in the enigma machine.
@author Josh Trujillo
'''

class Plugboard:
    def __init__(self, wiring):
        '''
        Args:
            wiring: List of tuple pairs with chars to substitute.

        Attributes:
            wiring: Dicionary with plug mappings.
                Two key:value pairs for each plug.
        '''
        self.wiring = {}
        for pair in wiring:
            print(pair)
            self.wiring[pair[0]] = pair[1]
            self.wiring[pair[1]] = pair[0]

    def swap(self, letter):
        '''
        Swaps the input letter with the plugged letter.

        Args:
            letter: The input letter.

        Returns:
            If letter is swapped, return value. If not, return the letter.
        '''
        if letter in self.wiring:
            return self.wiring[letter]
        else:
            return letter
