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
        if x // 100 and not x // 400:
            return False
        elif not x // 100:
            return True
        elif x // 400:
            return True
    if not x // 4:
        return False
