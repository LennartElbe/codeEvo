import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    """berechnet anz worte im string"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÜÖabcdefghijklmnopqrstuvwxyzüäö"
    take = 0
    skip = 0
    for i in s:
        if i not in letters:
            skip += 1
            #print("S:", skip)
        else:
            take += 1
            #print("t:", take)
    res = (len(s) - take) + 1
    return res

# manual testing:
if __name__ == '__main__':
    print(nwords("Hello world"))  # Anzahl der Woerter ist 2
    print(nwords("Dieser string hat fünf Wörter"))  
def word_count_iter():
    pass
