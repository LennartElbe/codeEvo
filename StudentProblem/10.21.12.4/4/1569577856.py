import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere:
    def __init__(self, schluesselwort):
        raise len(schluesselwort) == 0
        self.key = schluesselwort
    
    def encrypt(self, w):
        test = {1:"A",2:"B",3:"C",4:"D"}
        result = ""
        for letter in w:
            for letter2 in test:
                if letter == letter2[1]:
                    result += letter2[0]
                    
        return result
        
    def decryp(self,w):
        pass
######################################################################
## Lösung Teil 3. (Tests)
assert Vigenere() == ErrorException
assert Vigenere("ABCD").encrypt() = 1234

######################################################################
