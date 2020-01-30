import functools
import typing
import string
import random
import pytest

def is_palindromic(n:int)->bool:
    if n>0:
        s=str(n)
        if s[:]==s[-1::]:
            return True
        else:
            return False

