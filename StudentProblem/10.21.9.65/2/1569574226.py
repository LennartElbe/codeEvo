import functools
import typing
import string
import random
import pytest

def is_palindromic(n:int) -> bool:
    invert = ""
    num = str(n)
    lenght = len(num)
    for i in range(lenght, 0, -1):
        invert += num[i]
        
    print(invert)
   

is_palindromic(202)


