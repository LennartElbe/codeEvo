import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    """berechnet anz worte im string"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    take = 0
    skip = 0
    for i in s:
        if i not in letters:
            skip += 1
        else:
            take += 1
    res = (len(s) - take)+ skip
    return res
if __name__ == '__main__':
    print(len("Hello world")) # string hat Länge 11
    print(nwords("Hello world")) # Anzahl der Woerter ist 2

