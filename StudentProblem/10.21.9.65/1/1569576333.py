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
                break
        res += [word]
     count = len(res)
    return count
        

            
            

