import functools
import typing
import string
import random
import pytest

def leap(x):
    ''' Variablen:
              x = int: Das Jahr
    returns True oder Falsch
    '''
#x ist des zu Überprüfende Jahr    
    if x // 100 and not x // 400:
        return False
    elif x // 4:
        return True
