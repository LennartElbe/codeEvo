import functools
import typing
import string
import random
import pytest

def schaltjahr(jahr: int):
    if jahr // 4 or (jahr // 100 and not jahr // 400):
        return True:
    else:
        return False
