import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s):
    sep = True
    n = 0
    for c in s:
        if c == ' ' and not sep:
            sep = True
        elif c != ' ' and sep:
            sep = False
            n += 1
    return n


print(nwords(""))
print(nwords("   "))
print(nwords("dgjan"))
print(nwords("dgja n"))
print(nwords("dg   ja n"))
print(nwords("   jg   ja n   "))

## Lösung Teil 2.
def word_count_iter(it):
    nz = 0
    nw = 0
    nc = 0
    for z in it:
        nz += 1
        nw += nwords(z)
        nc += len(z)
    return nz, nw, nc

print(word_count_iter(["dg   ja n", "dg   ja n  "]))
######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
