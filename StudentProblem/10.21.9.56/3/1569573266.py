import functools
import typing
import string
import random
import pytest

def leap(jahrzahl: int) -> bool:
    'return True if the given year is schaltjahr and false if not'
    schaltjahr == True
    if jahrzahl > 1582:
        if jahrzahl % 100 == 0 and jahrzahl% 400 != 0:
            return schaltjahr
        else:
            return False
    else:
        print('jahrzahl ist kleiner als 1582')
