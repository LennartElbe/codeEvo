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
            print(i)
            if s[i] != ' ':
                word += s[i]
                i += 1
                print(i)
            else:
                break
        print(i)
        res += [word]
        i += 1
    return res
        
print(nwords("Mah moud"))
            
            

