import functools
import typing
import string
import random
import pytest

def divisors(n):
"""
Args: n
    n: Int

Dieser Funktion return eine Liste von Int werten für die gilt das n durch diese ohne Rest teilbar ist

Return: list"""
    L = []
    H = []
    l = n
    while l != 0:
        L.append(l)
        l -= 1
    for i in L:
        if n % i == 0:
            H.append(i)  
    return H
