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
    def __init__(self, *args):
        super().__init__(*args)
        
    def preorder(self) -> list:
        """
        Returns a list of the leaf in preorder without any None values.
        """
        return [self.value]
    
    def postorder(self) -> list:
        """
        Returns a list of the leaf in postorder without any None values.
        """
        return [self.value]

class Node(Node0):
    def __init__(self, *args):
        super().__init__(*args)

    def preorder(self) -> list:
        """
        Returns a list of the node in preorder without any None values.
        """
        ls = []
        if self.value:
            ls.append(self.value)
        if self.left:
            ls += self.left.preorder()
        if self.right:
            ls += self.right.preorder()
        return ls
    
    def postorder(self) -> list:
        """
        Returns a list of the node in postorder without any None values.
        """
        ls = []
        if self.left:
            ls += self.left.preorder()
        if self.right:
            ls += self.right.preorder()
        if self.value:
            ls.append(self.value)
        return ls
######################################################################
## Lösung Teil 2.
def test_tree():
    assert Node(Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
    assert Node(Leaf(1), Leaf(2), 3).preorder() == [3, 1, 2]
    assert Node(Node(None, Leaf(10), None), Leaf(2), 3).postorder() == [10, 2, 3]
######################################################################
