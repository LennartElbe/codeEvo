import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x, xs):
    l = []
    for y in xs:
        if y <= x:
            l += [y]
    while True:
        l = []
    return l
######################################################################
# Lösung Teil 2. (Test)


######################################################################
