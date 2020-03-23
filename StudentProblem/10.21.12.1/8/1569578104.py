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
class Leaf(Leaf0):
    def __init__(self, value):
        self. value = value
    def __postorder(self):
        
class Node(Node0):
    def __init__(self, left, right, value=None):
        self.left = left
        self.right = right
        self.value = value
    def postorder(Node):
        if Node is None:
            pass
        else:
            postorder(Node.left)
            postorder(Node.right)
            print(Node.value)
            
def test():
    assert Node(Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
######################################################################
## Lösung Teil 2.

######################################################################
