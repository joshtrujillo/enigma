'''
enigma.py
enigma machine simulator
@author Josh Trujillo
'''

from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

# Constants
VALID_ROTORS = ["I", "II", "III"]
VALID_REFLECTORS = ["A", "B"]
ALPHABET_SIZE = 26

class EnigmaMachine:
    def __init__(self, rotors, initial_positions, reflector, plugboard):
        '''
        Initialize the EnigmaMachine with rotors, reflector, and plugboard

        Args:
            rotors (list[str]): Rotor identifiers, e.g., ["I", "II", "III"].
            initial_posisions (list[int]): Initial rotor positions (0-25).
            reflector (str): Reflector type, e.g., "A" or "B".
            plugboard (str): Plugboard connections, e.g., "AB DF GE"

        Attributes: 
            rotors (list[Rotor]): Initialized rotor objects.
            reflector (Reflector): Reflector object.
            plugboard (Plugboard): Plugboard object.
        '''
        self.rotors = [Rotor(rotor, position) \
            for rotor, position in zip(rotors, initial_positions)]
        self.reflector = Reflector(reflector)
        self.plugboard = Plugboard(plugboard)

    def encrypt_letter(self, letter):
        '''
        Encrypts a single letter through the plugboard, rotors, reflector,
        back to rotors and the plugboard.

        Args:
            letter (str): The input letter.

        Returns:
            str: The output letter from the rotor.
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
            message (str): The message to encrypt.

        Returns:
            str: The output message.
        '''
        return ''.join(self.encrypt_letter(letter) for letter in message)

    def set_rotor_positions(self, positions):
        '''
        Sets the rotor positions to specified values.

        Args:
            positions (list[int]): List of ints for rotor positions (0-25)
        '''
        for position, rotor in zip(positions, self.rotors):
            rotor.position = position % ALPHABET_SIZE

    def step_rotors(self):
        '''Steps the rotors and handles the step cascade.'''
        if self.rotors[0].rotate():
            if self.rotors[1].rotate():
                self.rotors[2].rotate()

def get_rotor_input():
    rotors = []
    for i in range(1, 4):
        while True:
            rotor = input(f"Input rotor {i} (I, II, III): ")
            if rotor in VALID_ROTORS:
                rotors.append(rotor)
                break
            else:
                print("Invalid rotor. Please enter I, II, or III.")
    return rotors

def get_position_input():
    positions = []
    for i in range(1, 4):
        while True:
            try:
                pos = int(input(f"Input rotor position {i} (0-25): "))
                if 0 <= pos < ALPHABET_SIZE:
                    positions.append(pos)
                    break
                else:
                    print("Position must be between 0 and 25.")
            except ValueError:
                print("Invalid input. Enter an integer.")
    return positions

def get_reflector_input():
    while True:
        reflector = input("Input reflector (A, B): ")
        if reflector in VALID_REFLECTORS:
            return reflector
        print("Invalid reflector. Please enter A or B.")

def get_plugboard_input():
    plug_pairs = input("Input plugboard pairs (e.g. AR TG ...): ").upper().split()
    return plug_pairs


if __name__=="__main__":
    print("Enigma I simulator")
    
    rotors = get_rotor_input()
    positions = get_position_input()
    reflector = get_reflector_input()
    plugboard = get_plugboard_input()

    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    
    message = "".join(input("Enter your message: ").upper().split())
    ciphertext = machine.encrypt_message(message)
    
    print("Ciphertext:")
    print(ciphertext)
