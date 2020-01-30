import functools
import typing
import string
import random
import pytest

def nwords(s: string):
    """counts the number of words in input string n
    args: s: string with words to be counted
    returns: anzahl: number of words in sting """
    temp = 0
    anzahl = 0
    for i in s:
        if i == string.whitespace:
            temp += 1
        if i != string.whitespace and temp != 0:
            temp = 0
            anzahl += 1
    return anzahl
def word_count_iter (it):
    """counts the number of words in input string
    args: it: input string
    returns: tuple with the number of lines, words and symbols in it (in this order)"""
    zahl = nwords (it)
    nummer = 0
    for i in it:
        nummer += 1
    return tuple (["?",zahl,nummer])
