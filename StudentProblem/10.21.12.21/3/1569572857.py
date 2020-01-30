import functools
import typing
import string
import random
import pytest

def leap(jz: int) -> bool:
    """ leap year wenn durch 4 teilbar, ODER durch 100 und 400 teilbar, wenn 100 aber nicht 400 normales jahr
        jz muss >= 1582 sein
       
    """
    if jz >= 1582:
        if jz // 4:
            print(jz, "ist ein Schaltjahr")
            return True
        elif jz // 100:
            if jz // 400:
                print(jz, "ist ein Schaltjahr")
                return True
            else:
                print(jz, "ist KEIN Schaltjahr")
                return False

print(leap(2004))
print(leap(2005))
