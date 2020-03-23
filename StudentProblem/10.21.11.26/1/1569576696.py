import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str):
    """Calculates the number of words in a string
    
    Args:
        s(str): a string s
    Return:
        An integer >= 0
    """
    count = 0
    if s ="":
        return 0
    else:
        for i in range(len(s)):
            if s[i] != " " and s[i + 1] == " ":
                count = count + 1
        return count
## Lösung Teil 2.
def word_count_iter(s):
    """Calculates the number of rows and words of an iterable object
    
    Args:
        iteralble object s(str/list/tupel)
    
    Return:
        tupel with number of rows and words of the iterable object
    """
    s = ""
    count_row = 0
    for i in s:
        s += "i"
    count_row = count_row + 1
    return [count_row, nwords(s)]
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    s = "Hey, what up"
    assert(word_count_iter(s) == [1, 3])
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f: str) :
    with open(f) as g:
        count = 0
        count_words = n(words(g))
        for i in g:
            count = count + 1
        return [-, count_words, count]
######################################################################
