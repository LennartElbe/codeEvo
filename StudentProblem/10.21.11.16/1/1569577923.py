import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    for i in s:
        for f in range(i, string.whitespace):
            i += 1
def word_count_iter(m: str):
    counter = ()
    for i in m:
       counter.append(i)
    for j in (i, string.whitespace):
        counter.append(j)
        
