import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere:
    def __init__(self, schluesselwort):
        #raise len(schluesselwort) == 0
        self.__key = schluesselwort
    
    def encrypt(self, w):
        test = {1:"A",2:"B",3:"C",4:"D"}
        result = ""
        for letter in w:
            for letter2 in test:
                if letter == str(letter2)[1]:
                    result += letter2[0]            
        return result
        
    def decryp(self,w):
        test = {1:"A",2:"B",3:"C",4:"D"}
        result = ""
        w2 = str(w)
        for letter in w2:
            for letter2 in test:
                if letter == letter2[0]:
                    result += letter2[1]            
        return result
######################################################################
## Lösung Teil 3. (Tests)
assert Vigenere("ABCD").encrypt("ABCD") == "1234"
assert Vigenere("1234").encrypt("1234") == "ABCD"

######################################################################
