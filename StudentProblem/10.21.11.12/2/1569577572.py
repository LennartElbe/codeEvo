import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> int:
    if n <= 0:
        print("n ist kein Palindrom")
    else:
        str_n = str(n)
        i = len(str_n) - 1
        n_reverse = []
        while i != -1:
            n_reverse.append(str_n[i])
            i -= 1
        for x in len(str_n):
            if str_n[x] == n_reverse[x]:
                continue
            else:
                print("n ist kein Palindrom")
        print("n ist ein Palindrom")
   

is_palindromic(123)
