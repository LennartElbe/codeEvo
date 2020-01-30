import functools
import typing
import string
import random
import pytest

def list_filter(x , xs) -> list:
    ls = []
    for i in xs:
        if i <= i:
            ls.append(i)
    return ls
