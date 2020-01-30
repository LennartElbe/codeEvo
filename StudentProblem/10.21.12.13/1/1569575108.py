import functools
import typing
import string
import random
import pytest

def nwords(s: string) -> int:
    """Function to give the amount of words in a string
    args: s: string which gets counted
    """
    if s == "":
        return 0
    else:
        counter = 1
        for i in s:
            if i == " ":
                counter += 1
        return counter
    
def test_nwords():
    assert nwords("hallo du") == 2
        
        
        
        
        
        
        
        
        
s = "sa xa"

