import pytest
from .enigma import EnigmaMachine
from .rotor import Rotor
from .plugboard import Plugboard
from .reflector import Reflector


def test_rotor_forward_sub():
    rotor = Rotor("I")
    assert rotor.forward_substitute("A") == "E"


def test_rotor_backward_sub():
    rotor = Rotor("I")
    assert rotor.backward_substitute("E") == "A"


def test_rotor_step():
    rotors = ["I", "II", "III"]
    positions = [0, 0, 0]
    reflector = "A"
    plugboard = "AV"
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    message = "A" * 5
    machine.encrypt_message(message)
    assert machine.rotors[0].position == 5
    machine.set_rotor_positions([0, 0, 0])
    message = "A" * 27
    machine.encrypt_message(message)
    assert machine.rotors[1].position == 1


def test_plugboard():
    plugboard = Plugboard("EA FN")
    assert plugboard.swap("E") == "A"
    assert plugboard.swap("A") == "E"
    assert plugboard.swap("F") == "N"
    assert plugboard.swap("N") == "F"
    assert plugboard.swap("Z") == "Z"


def test_reflector():
    reflector = Reflector("A")
    assert reflector.reflect("A") == "E"


def test_set_rotor_positions():
    rotors = ["I", "II", "III"]
    positions = [0, 0, 0]
    reflector = "A"
    plugboard = ""
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    machine.set_rotor_positions([23, 3, 21])
    assert machine.rotors[0].position == 23
    assert machine.rotors[1].position == 3
    assert machine.rotors[2].position == 21


def test_enigma_encrypt_decrypt_letter():
    rotors = ["I", "II", "III"]
    positions = [0, 0, 0]
    reflector = "A"
    plugboard = ""
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)
    plain_letter = "A"
    cipher_letter = machine.encrypt_letter(plain_letter)
    machine.set_rotor_positions(positions)
    assert machine.encrypt_letter(cipher_letter) == plain_letter


def test_enigma_encrypt_decrypt():
    rotors = ["I", "II", "III"]
    positions = [0, 0, 0]
    reflector = "A"
    plugboard = "AV"
    machine = EnigmaMachine(rotors, positions, reflector, plugboard)

    message = "HEREISALONGERMESSAGETOTESTMYENIGMAMACHINESIMULATORWITHLETSSEEHOWITHANDLESTHISONE"
    ciphertext = machine.encrypt_message(message)
    machine.set_rotor_positions([0, 0, 0])
    plaintext = machine.encrypt_message(ciphertext)
    assert plaintext == message
