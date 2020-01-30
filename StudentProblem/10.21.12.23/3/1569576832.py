import functools
import typing
import string
import random
import pytest

def leap(x):
    ''' Variablen:
              x = int: Das Jahr
    returns True oder False
    '''
#x ist des zu Überprüfende Jahr    
    if x // 4:
        if x // 400 and not x // 100:
            return True
    else:
        return False
