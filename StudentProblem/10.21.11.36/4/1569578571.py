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
    shifting = (ord(k) - 65) % 25
    return chr(ord(s) + shifting)

def shift_back(s, k):
    """Helper function to shift a letter s back according to k. 
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
        key_mult = self.key * (len(w)//len(self.key) + 1)
        enc = ""
        for ind, ch in enumerate(w):
            enc += shift(ch, key_mult[ind])
        return enc
    
    def decrypt(self, w: str):
        """Decrypts a given text using the class key.
        Args:
            w: The text to be encrypted
        """
        key_mult = self.key * (len(w)//len(self.key) + 1)
        enc = ""
        for ind, ch in enumerate(w):
            enc += shift_back(ch, key_mult[ind])
        return enc
    
    
    
            
            
            
        
        
        
        
    def decrypt(self, w):
        pass
######################################################################
## Lösung Teil 3. (Tests)
def test_Vigenere():
    t = Vigenere("A")
    assert t.encrypt("HELLO") == "HELLO"
    t2 = Vigenere("B")
    assert t.encrypt("HELLO") == "IFMMP"
######################################################################
