import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """This function tests wether a positive integer s a palindrome or not
       A Palindrome is a Number where its the same read backwards
       Examples:
       is_palindromic(1001) == True
       is_palindromic(1000) == False
       """
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
