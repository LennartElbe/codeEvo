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
    lst = []
    def postorder(Node):
        if leaf is None:
            pass
        else:
            postorder(Node.left)
            postorder(Node.right)
            lst.append(value)
        return lst

    def preorder(Node):
        lst = []
        if leaf is None:
            pass
        else:
            lst.append(value)
            postorder(Node.left)
            postorder(Node.right)
        return lst
             

class Node(Node0):
    lst = []
    def postorder(Node):
        if leaf is None:
            pass
        else:
            postorder(Node.left)
            postorder(Node.right)
            lst.append(value)
        return lst

    def preorder(Node):
        lst = []
        if leaf is None:
            pass
        else:
            lst.append(value)
            postorder(Node.left)
            postorder(Node.right)
        return lst        
######################################################################
## Lösung Teil 2.
def test_trees():
    Node = Node(Leaf(1), Leaf(2), 3)
    assert postorder(Node) == [1, 2, 3]
######################################################################
