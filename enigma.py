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
        self.rotors = [Rotor(rotor, position) for rotor, position in zip(rotors, initial_positions)]
        self.reflector = Reflector(reflector)
        self.plugboard = Plugboard(plugboard)

    def encrypt_letter(self, letter):
        '''
        passes a letter to the plugboard, rotors, reflector,
        back to rotors and the plugboard
        '''
        letter = self.plugboard.swap(letter)
        self.step_rotors()
        for rotor in self.rotors:
            letter = rotor.forward_substitute(letter)
        letter = self.reflector.reflect(letter)
        for rotor in self.rotors:
            letter = rotor.backward_substitute(letter)
        return self.plugboard.swap(letter)

    def encrypt_message(self, message):
        '''
        encrypts a message using encrypt_letter
        '''
        result = ""
        for letter in message:
            result += str(self.encrypt_letter(letter))
        return result

    def set_rotor_positions(self, positions):
        for position, rotor in zip(positions, self.rotors):
            rotor.position = position

    def step_rotors(self):
        '''
        steps the rotors and handles the step cascade
        '''
        if self.rotors[0].rotate():
            if self.rotors[1].rotate():
                self.rotors[2].rotate()


if __name__=="__main__":
    rotors = ["I", "II", "III"] 
    positions = [0, 0, 0]
    reflector = "A"
    plugboard = [("A", "V")]
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    
    message = "HELLOWORLD"
    print(machine.encrypt_message(message))

