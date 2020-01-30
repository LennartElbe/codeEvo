import functools
import typing
import string
import random
import pytest

def nwords(s:str) -> list:
    res = []
    i = 0
    n = len(s)
    while i < n:
        word = ''
        while True:
            if s[i] != ' ':
                word += s[i]
                i += 1
            else:
                i += 1
                break
        res += [word]
        i += 1
    return res
        
print(nwords("Mah moud"))
            
            

