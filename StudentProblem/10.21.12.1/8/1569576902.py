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

class Leaf(Leaf0):
    def __init__(self, value):
        self. value = value
    
    def preorder(Leaf):
        if 
        else:
            postorder

class Node(Node0):
    def __init__(self, left, right, value=None):
        self.left = left
        self.right = right
        self.value = value
    def postorder(Node):
        if Node is None:
            pass
        else:
            return[postorder(Node.left), postorder(Node.right), Node.value]
            
def test():
    assert  Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
