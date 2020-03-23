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
        super().__init__(value)
        
        
class Node(Node0):
    def __init__(self, left, right, value):
        super().__init__(left, right, value)
        
    def perorder(self):
        res = []
        if self.value is None:
            pass
        else:
            res += [self.value]
            self.preorder(self.left)
            self.perorder(self.right)
        return res
            
            
    def postorder(self):
        res = []
        if self.value is None:
            pass
        else:
            self.preorder(self.left)
            self.perorder(self.right)
            res += [self.value]
        return res
        
######################################################################
## Lösung Teil 2.
def test_Node():
    n = Node(Leaf(1), Leaf(2), 3)
    n.perorder() == [3, 1, 2]
######################################################################
