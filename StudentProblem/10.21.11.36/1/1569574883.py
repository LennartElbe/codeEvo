import functools
import typing
import string
import random
import pytest

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
        
print(word_count_iter(["     ", ",,,,,"]))    