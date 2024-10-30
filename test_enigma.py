import pytest 
from enigma import EnigmaMachine
from rotor import Rotor
from plugboard import Plugboard
from reflector import Reflector

def test_rotor_forward_sub():
    rotor = Rotor("I")
    assert rotor.forward_substitute("A") == "E"

def test_rotor_backward_sub():
    rotor = Rotor("I")
    assert rotor.backward_substitute("E") == "A"
    

def test_plugboard():
    plugboard = Plugboard([("E", "A")])
    assert plugboard.swap("E") == "A"
    assert plugboard.swap("Z") == "Z"

def test_reflector():
    reflector = Reflector("A")
    assert reflector.reflect("A") == "E"

def test_enigma_encrypt_letter():
    rotors = ["I", "II", "III"] 
    positions = [0, 0, 0]
    reflector = "A"
    plugboard = [("A", "V")]
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    pass

def test_enigma_encrypt_decrypt():
    rotors = ["I", "II", "III"] 
    positions = [0, 0, 0]
    reflector = "A"
    plugboard = [("A", "V")]
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    
    message = "AAAAAAA"
    breakpoint()
    ciphertext = machine.encrypt_message(message)

    machine.set_rotor_positions([0,0,0])

    plaintext = machine.encrypt_message(ciphertext)

    assert plaintext == message


