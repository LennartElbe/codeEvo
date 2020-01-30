import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    """Calculates the number of words in a string
    
    Args:
        s(str): a string s
    Return:
        An integer >= 0
    """
    count = 0
    if s == "":
        return 0
    else:
        for i in range(len(s)):
            if s[i] != " " and s[i + 1] == " ":
                count = count + 1
        return count
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
