import functools
import typing
import string
import random
import pytest

# HHHHH
# WORLD

def shift(s, k):
    """Helper function to shift a letter s according to k. 
    """
    shifting = ord(k) - 97
    return chr(ord(s) + shifting)
    


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
