import functools
import typing
import string
import random
import pytest

class Vigenere:
    def __init__(self , key):
        if key is not None:
            self.key =  key
        else:
            raise AttributeError
    
    def encrypt(w:str):
        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
             'X', 'Y', 'Z']
        k  = 0
        for i in range(0, len(w)):
            if k >= len(self.key):
               k = 0
            a = ord(i) + (ord(self.key[k]) - 65)
            if a > 90:
                a = 65 + (a - 90)
            a = a - 65
            w[i] = l[a]
            k = k + 1
     
    def encrypt(w:str):
        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
             'X', 'Y', 'Z']
        k  = 0
        for i in range(0, len(w)):
            if k >= len(self.key):
                k = 0
            a = ord(i) - (ord(self.key[k]) - 65)
            if a < 65:
                a = 90 - (65 - a)
            a = a - 65
            w[i] = l[a]
            k = k + 1
