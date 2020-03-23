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
            # if its not whitespace, its a letter
            current_word += ch
        else:
            # only append word if its actually a word
            # (not only whitespace characters before)
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
    lines, words, chars = 0, 0, 0
    for i in it:
        lines += 1
        words += nwords(i)
        chars += len(i)
    return lines, words, chars
   
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    iter1 = ["Hello, World", "Hallo, Welt"]
    iter2 = ["     "]
    iter3 = ("Hello", "World")
    assert word_count_iter(iter1) == (2, 4, 23)
    assert word_count_iter(iter2) == (1, 0, 5)
    assert word_count_iter(iter3) == (2, 2, 10)
    
    
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f: str) -> tuple:
    """Takes the name of a textfile and counts the number of chars, words and lines
    Args:
        f (str): Name of a textfile
    Returns:
        tuple: number of lines, words and chars
    """
    lines, words, chars = 0, 0, 0
    
            
        
######################################################################
