import pytest
from caesercipher import encrypt, decrypt, enter_message
from unittest.mock import patch

def test_encrypt_with_input_mock():
    with patch('builtins.input', side_effect=['e', 'HELLO', '3']):
        mode, message, shift = enter_message() 
        assert encrypt(message, shift) == 'KHOOR'
        
    with patch('builtins.input', side_effect=['e', 'WORLD', '5']):
        mode, message, shift = enter_message() 
        assert encrypt(message, shift) == 'BTWQI'
    
    with patch('builtins.input', side_effect=['e', 'HELLO WORLD', '4']):
        mode, message, shift = enter_message() 
        assert encrypt(message, shift) == 'LIPPS ASVPH'

    with patch('builtins.input', side_effect=['e', 'HELLO WORLD###', '27']):
        mode, message, shift = enter_message() 
        assert encrypt(message, shift) == 'IFMMP XPSME###'

def test_decrypt_with_input_mock():
    with patch('builtins.input', side_effect=['d', 'KHOOR', '3']):
        mode, message, shift = enter_message() 
        assert decrypt(message, shift) == 'HELLO'

    with patch('builtins.input', side_effect=['d', 'BTWQI', '5']):
        mode, message, shift = enter_message() 
        assert decrypt(message, shift) == 'WORLD'

    with patch('builtins.input', side_effect=['d', 'LIPPS ASVPH', '4']):
        mode, message, shift = enter_message() 
        assert decrypt(message, shift) == 'HELLO WORLD'

    with patch('builtins.input', side_effect=['d', 'IFMMP XPSME###', '27']):
        mode, message, shift = enter_message() 
        assert decrypt(message, shift) == 'HELLO WORLD###'

