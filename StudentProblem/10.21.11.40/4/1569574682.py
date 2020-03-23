import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
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
        new_key = self.key * (len(w) // len(self.key) + 1)
        msg = ""
        for i, c in enumerate(w):
            new_c = chr(ord(c) + (ord(new_key[i]) - ord('A')))
            if ord(new_c) > ord('Z'):
                new_c = chr(ord(new_c) - 26)
            msg += new_c
        return msg
                        
    def decrypt(self, w: str) -> str:
        """
        Decrypts the given text with the secret key of the object.
        """
        new_key = self.key * (len(w) // len(self.key) + 1)
        msg = ""
        for i, c in enumerate(w):
            new_c = chr(ord(c) - (ord(new_key[i]) - ord('A')))
            if ord(new_c) < ord('A'):
                new_c = chr(ord(new_c) + 26)
            msg += new_c
        return msg
######################################################################
## Lösung Teil 3. (Tests)
def test_vigenere():
    v1 = Vigenere("MYSECRETKEY")
    assert v1.decrypt(v1.encrypt("TESTFOOBAR")) == "TESTFOOBAR"
    
    v2 = Vigenere("AAA")
    assert v2.encrypt("BBB") == "BBB"
    
    assert Vigenere("ABCD").encrypt("DCBA") == "DEFG"
######################################################################
