import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere():
    """"""
    def __init__(self, key):
        """"""
        if key == "":
            raise TypeError("Key darf nicht leer sein")
        else:
            self.key = key
    def encrypt(self, w: str) -> str:
        """encrypts the string"""
        o = ""
        for i in range(len(w)):
            a = ord(w[i])
            b = ord(self.key[i])
            c = a + b
            if c > 25:
                c = c - 25
            o = o + c
        return o
        
        
    def decrypt(self, w: str) -> str:
        """"""
        for i in w:
            a = 1
            

c = Vigenere("A")
print(c.encrypt())
    
######################################################################
## Lösung Teil 3. (Tests)

######################################################################
