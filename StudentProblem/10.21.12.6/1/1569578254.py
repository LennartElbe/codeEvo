import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Function to compute the number of words in a string.
    
    Args:
        s(str): A given string.
        
    Returns:
        r(int): Number of words in the string.
    """
    res = []
    for element in s:
        res.append(element)
    return len(res)


## Lösung Teil 2.
def word_count_iter():
    """
    """
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    testlist1 = ["This is not a test."]
    assert word_count_iter(testlist1) == (1, 5, 15)
    assert word_count_iter() == ()
    assert word_count_iter() == ()
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f) -> tuple:
    """Count the number of lines, letters and words in a given document.
    
    Args:
        f(filename): A file containing text.
    Returns:
        A tuple containing the counted lines, words, and letters in f
    """
    ...
    lnc = line_count
    wc = word_count
    lc = lettercount
    ...
    return (lnc, wc, lc)
######################################################################
