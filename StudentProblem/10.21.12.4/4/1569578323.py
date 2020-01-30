import functools
import typing
import string
import random
import pytest

class Vigenere:
    def __init__(self, schluesselwort):
        raise len(schluesselwort) == 0
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
