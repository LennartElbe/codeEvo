import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    result = []
    for i in s:
        if i == " ":
            x = s.index(i)
            y = s[:x + 1]
            s = s[x + 2:]
            result.append(y)
        else:
            result.append(s)
    return result

def test_11():
    assert nwords("Hallo ") == ["Hallo "]
## Lösung Teil 2.

######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f: file):
    line_num = 0
    word_num = 0
    ze_num = 0
    with open(r, f) as e:
        for line in e:
            line_num += 1
            x = line.split()
            for i in x:
                word_num += 1
                for j in i:
                    ze_num+= 1
    return(line_num, word_num, ze_num)
######################################################################
