import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
# HHHHH
# WORLD
class VigenereException(Exception):
    pass

class Vigenere:
    """A class to do Vigenere Encoding and Decoding. 
    Attributes:
        key: list
    """
    def __init__(self, key: str):
        if len(key) > 1:
            raise VigenereException ("Key must contain actual characters")
        else:
            self.key = key
    
    def encrypt(self, w: str):
        """Encrypts a given text using the class key.
        Args:
            w: 
        """
        pass
        
        
        
    def decrypt(self, w):
        pass
######################################################################
## Lösung Teil 3. (Tests)
h = 2
s = 5
print(s // h)
######################################################################
