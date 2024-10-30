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
        '''
        Args:
            rotors: A list of strings for rotors e.g. "I"
            initial_posisions: A list of ints for rotor startings positions
            reflector: String for the reflector.
            plugboard: List of tuples of character pairs e.g. [("A", "V")]

        Attributes: 
            rotors: A list of rotor objects
            reflector: Reflector object
            plugboard: Plugboard object
        '''
        self.rotors = [Rotor(rotor, position) \
            for rotor, position in zip(rotors, initial_positions)]
        self.reflector = Reflector(reflector)
        self.plugboard = Plugboard(plugboard)

    def encrypt_letter(self, letter):
        '''
        Passes a letter to the plugboard, rotors, reflector,
        back to rotors and the plugboard.

        Args:
            letter: The input letter.

        Returns:
            The output letter from the rotor.
        '''
        letter = self.plugboard.swap(letter)
        self.step_rotors()
        for rotor in self.rotors:
            letter = rotor.forward_substitute(letter)
        letter = self.reflector.reflect(letter)
        for rotor in reversed(self.rotors):
            letter = rotor.backward_substitute(letter)
        return self.plugboard.swap(letter)

    def encrypt_message(self, message):
        '''
        Encrypts a message using encrypt_letter.

        Args:
            message: The message to encrypt

        Returns:
            The output message
        '''
        result = ""
        for letter in message:
            result += str(self.encrypt_letter(letter))
        return result

    def set_rotor_positions(self, positions):
        '''
        Sets the rotor positions.

        Args:
            positions: List of ints for rotor positions
        '''
        for position, rotor in zip(positions, self.rotors):
            rotor.position = position

    def step_rotors(self):
        '''Steps the rotors and handles the step cascade.'''
        if self.rotors[0].rotate():
            if self.rotors[1].rotate():
                self.rotors[2].rotate()


if __name__=="__main__":
    valid_rotors = ["I", "II", "III"]
    print("Enigma I emulator")
    
    rotors = []
    rotors[0] = input("Please input rotor 1 (I, II, III): ")
    rotors[1] = input("Please input rotor 2 (I, II, III): ")
    rotors[2] = input("Please input rotor 3 (I, II, III): ")

    positions = []

    '''
    rotors = ["I", "II", "III"] 
    positions = [0, 0, 0]
    reflector = "B"
    plugboard = []
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    
    message = "A" * 27
    for letter in message:
        print(machine.encrypt_letter(letter))
        for i, rotor in enumerate(machine.rotors):
            print("%d rotor position : %d" % (i, rotor.position))

    '''
