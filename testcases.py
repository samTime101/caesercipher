import pytest
from caesercipher import encrypt, decrypt
from unittest.mock import patch
from caesercipher import enter_message

def test_encrypt():
    assert encrypt('HELLO', 3) == 'KHOOR'
    assert encrypt('WORLD', 5) == 'BTMJI'

def test_decrypt():
    assert decrypt('KHOOR', 3) == 'HELLO'
    assert decrypt('BTMJI', 5) == 'WORLD'

def test_encrypt_with_input_mock():
    with patch('builtins.input', side_effect=['e', 'HELLO', '3']):
        mode, message, shift = enter_message() 
        assert encrypt(message, shift) == 'KHOOR'
