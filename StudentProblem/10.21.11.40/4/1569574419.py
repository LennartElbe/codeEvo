import functools
import typing
import string
import random
import pytest

class Vigenere:
    def __init__(self, key: str):
        """
        Create object with a secret key.
        """
        assert key
        self.key = key
    
    def encrypt(self, w: str) -> str:
        """
        Encrypt the given text with the secret key of the object.
        """
        new_key = self.key * (len(w) // len(self.key))
        msg = ""
        for i, c in enumerate(w):
            new_c = ord(chr(c) + (new_key[i] - chr('A'))
            if new_c > chr('Z'):
                new_c -= 26
            msg += new_c
        return msg
                        
        def decrypt(self, w: str) -> str:
        """
        Decrypts the given text with the secret key of the object.
        """
        new_key = self.key * (len(w) // len(self.key))
        msg = ""
        for i, c in enumerate(w):
            new_c = ord(chr(c) - (new_key[i] - chr('A'))
            if new_c < chr('A'):
                new_c += 26
            msg += new_c
        return msg
