import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
# HHHHH
# WORLD

def shift(s, k):
    """Helper function to shift a letter s according to k. 
    """
    pass


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
            w: The text to be encrypted
        """
        key_mult = key * (len(w)//len(key) + 1)
        enc = ""
        for ind, ch in enumerate(w):
            enc += shift(ch, key_mult[ind])
        return enc
            
            
            
        
        
        
        
    def decrypt(self, w):
        pass
######################################################################
## Lösung Teil 3. (Tests)
print(ord(a))
######################################################################
