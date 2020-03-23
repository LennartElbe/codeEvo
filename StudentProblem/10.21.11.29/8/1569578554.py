import functools
import typing
import string
import random
import pytest


class Leaf0:
  def __init__ (self, value):
    self.value = value

class Node0:
  def __init__ (self, left, right, value=None):
    self.value = value
    self.left = left
    self.right = right

## Lösung Teil 1.

######################################################################
## Lösung Teil 2.
def test_leaf():
    assert(Node(Leaf(1), Leaf(2), 3)).postorder() == [1,2,3]
    assert(Node(Leaf(1), Leaf(2)).postorder() == [1,2]
######################################################################
