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
        sword = self.key
        while len(sword) < len(w):
            sword = sword + sword
        o = ""
        for i in range(len(w)):
            a = ord(w[i]) -65
            b = ord(sword[i]) -65
            c = a + b
            if c > 25:
                c = c - 25
            o = o + chr(c  + 65)
        return o
        
        
    def decrypt(self, w: str) -> str:
        """"""
        sword = self.key
        while len(sword) < len(w):
            sword = sword + sword
        o = ""
        for i in range(len(w)):
            a = ord(w[i]) -65
            b = ord(sword[i]) -65
            c = a - b
            if c < 0:
                c = c + 25
            o = o + chr(c  + 65)
        return o
            
c = Vigenere("A")
a = c.encrypt("HALLO")
b = decrypt(a)
print(a, b)


    
######################################################################
## Lösung Teil 3. (Tests)

######################################################################
