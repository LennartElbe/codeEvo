import functools
import typing
import string
import random
import pytest

def leap(n:int)->bool:
    if n>1582:
        if n % 4==0:
            return True
        elif n % 400==0:
            return True
        else:
            return False
    else:
        print('please enter a year number >1582')
        
print(leap(2000))

