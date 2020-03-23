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
def peroder(Node0):
    if Node0 is None:
        return None
    else:
        perpder(self.value)
        perpder(self.left)
        perpder(self.right)

        
def postorder(Node0):
    if Node0 is None:
        return None
    else:
        postorder(self.left)
        postorder(self.right)
        postorder(self.value)
######################################################################
## Lösung Teil 2.
def test_1():
    assert  Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
    assert  Node (Leaf(1), Leaf(2)).postorder() == [1,2]
    assert  Node (Leaf(1), Leaf(2), 3).peroder() == [3, 1, 2]
    assert  Node (Leaf(1), Leaf(2)).peroder() == [1, 2]
######################################################################
