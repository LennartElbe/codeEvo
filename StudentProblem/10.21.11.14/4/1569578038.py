import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere():
    """Class Vigenere
    """
    def __init__(self, key):
        self.key = key
        
    def encrypt(w: str):
        z = key * len(w)
        return ord(z)
        
            
    
    def decrypt(wcrypt: str):
        return chr(wcrypt)
        
        
        
    
######################################################################
## Lösung Teil 3. (Tests)
def test_enc():
    assert encrypt(Hello)
    
def test_dec():
    assert decrypt()
######################################################################
