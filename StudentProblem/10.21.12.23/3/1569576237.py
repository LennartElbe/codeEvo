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
    if x // 4:
        if x not // 100 and x // 400:
            return True
    else:
        return False
