import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Count the number of words in a given string. Words are separated by at least one char in string.whitespace
    Args:
        s (str): A string whose words are counted
    Returns: 
        int: Number of words in the given string
    """
    n = 0
    words = []
    current_word = ""
    for ch in s:
        if ch not in string.whitespace:
            current_word += ch
        else:
            if len(current_word) > 0:
                words.append(current_word)
                current_word = ""
    if len(current_word) > 0:
        words.append(current_word)
    return len(words)

## Lösung Teil 2.
def word_count_iter(it) -> tuple:
    """Takes an iterable that yields a str in every iteration and returns a tuple
    with the number of lines, words and characters
    Args:
        it (iterable)
    Returns: 
        tuple 
    """
    # lines, words, chars 
    counts = (0, 0, 0)
    for i in it:
        counts[0] += 1
        counts[1] += nwords(i)
        counts[2] += len(i)
    return counts
        
    
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    iter1 = ["Hello, World", "Hallo, Welt"]
    assert word_count_iter(iter1) == (2, 4, 23)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
