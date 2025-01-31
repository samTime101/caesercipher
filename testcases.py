import pytest
from caesercipher import encrypt, decrypt

def test_encrypt():
    assert encrypt('HELLO', 3) == 'KHOOR'
    assert encrypt('WORLD', 5) == 'BTMJI'

def test_decrypt():
    assert decrypt('KHOOR', 3) == 'HELLO'
    assert decrypt('BTMJI', 5) == 'WORLD'

