import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Tests if a given number is a palindrome.
    Args:
        A natural number n.
    Returns:
        If the number is a palindrome or not.
    """
    
    if n > 0:
        if str(n) == str(n[::-1])
        return True
    else:
        return False
    
