'''
enigma.py
enigma machine simulator
@author Josh Trujillo
'''

from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

class EnigmaMachine:
    def __init__(self, rotors, initial_positions, reflector, plugboard):
        self.rotors = [Rotor(rotor, initial_positions(i)) for rotor, i in enumerate(rotors)]
        self.reflector = Reflector(reflector)
        self.plugboard = Plugboard(plugboard)

    def encrypt_letter(self, letter):
        # encrypt a single letter
        letter = self.plugboard.swap(letter)
        self.step_rotors()
        for rotor in self.rotors:
            letter = rotor.forward_substitute(letter)
        letter = self.reflector.reflect(letter)
        for rotor in self.rotors:
            letter = rotor.backward_substitute
        return self.plugboard.swap(letter)

    def encrypt_message(self, message):
        # encrypt a message letter by letter
        result = ""
        for letter in message:
            result += str(self.encrypt_letter(letter))
        return result

    def set_rotor_positions(self, positions):
       pass

    def step_rotors(self):
        '''
        steps the rotors and handles the step cascade
        '''

        pass
