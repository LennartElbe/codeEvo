import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s:str)->int:
    count=0
    n=len(s)
    for i in s:
        if i==' ':
            count+=1
    result=n-count
    return result
    
      
    
## Lösung Teil 2.

######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
