import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> Bool:
    n > 0
    for i in str(n) range(1:len(str(n)):-1): # rückwärts die zahl auslesen als string
        p = str(n) #vorwärts
            if i == p:
                return True
            else:
                return False
