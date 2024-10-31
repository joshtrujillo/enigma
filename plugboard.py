'''
plugboard.py
Class representing the plugboard in the enigma machine.
@author Josh Trujillo
'''

class Plugboard:
    def __init__(self, wiring):
        '''
        Args:
            wiring (str): Plugboard wiring e.g., "AD FV SE".

        Attributes:
            wiring (dict): Dicionary with plug mappings.
                Two key:value pairs for each plug.
        '''
        self.wiring = {}
        if len(wiring) > 2:
            plug_list = wiring.split()
            for pair in plug_list:
                if pair[0] not in self.wiring:
                    self.wiring[pair[0]] = pair[1]
                    self.wiring[pair[1]] = pair[0]
        elif len(wiring) == 2:
            self.wiring[wiring[0]] = wiring[1]
            self.wiring[wiring[1]] = wiring[0]

    def swap(self, letter):
        '''
        Swaps the input letter with the plugged letter.

        Args:
            letter (str): The input letter.

        Returns:
            str: If letter is swapped, return value. If not, return the letter.
        '''
        return self.wiring[letter] if letter in self.wiring else letter
