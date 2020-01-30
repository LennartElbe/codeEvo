import functools
import typing
import string
import random
import pytest

class Vigenere:
    def__init__(self , key):
        if key is not None:
            self.key =  key
        else:
            raise AttributeError
    
    def encrypt(w:str) 
