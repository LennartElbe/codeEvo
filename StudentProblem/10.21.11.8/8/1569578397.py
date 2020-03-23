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
    """An underclass of Leaf0 representing leaves in a tree."""
    def __init__(self, value):
        """The defining funciton of the class.
        Args:
            value: the value of the leaf
        """
        self.value = value
        
    
    def postorder(self):
        """A function that implements the post order notation
        of a leaf.
        
        It returns the value of the leaf. If it is none that it won't
        be added."""
        if self.value is None:
            return
        else:
            return self.value
        
    def preorder(self):
        """A function that implements the post order notation
        of a leaf.
        
        It returns the value of the leaf.f it is none that it won't
        be added."""
        if self.value is None:
            return
        else:
            return self.value
        
class Node(Node0):
    """An underclass of Node0, representing the node of a tree."""
    def __init__(self, left, right, value):
        """The defining function of the class."""
        self.left = left
        self.right = right
        self.value = value
        
    def preorder(self):
        """A function that implements the preorder method of a 
        given node object.
        
        It returns the ordered tree in pre order notation.
        If the value of a given node is None, than it won't be added
        to the output, but it's leaves will.
        
        Args:
            a node object
        Returns:
            a list of the pre order notation of the node.
        """
        if self.value is None:
            return[preorder(self.left),
                   preorder(self.right)]
        else:
            return[preorder(self,value),
                   preorder(self.left),
                   preorder(self.right)]
         
    def postorder(self):
        """A function that implements the post order method of a 
        given node object.
        
        It returns the ordered tree in post order notation.
        If the value of a given node is None, than it won't be added
        to the output, but it's leaves will.
        
        Args:
            a node object
        Returns:
            a list of the post order notation of the node.
        """
        if self.value is None:
            return [postorder(self.left),
                    postorder(self.right)]
        else:
            return [postorder(self.left),
                    postorder(self.right),
                    postorder(self.value)]
######################################################################
## Lösung Teil 2.
def test_postorder():
    assert Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
    assert Node (Leaf(1), Leaf(2)).postorder() == [1,2]
    assert Node (Leaf(), Leaf(), 3).postorder() == [3]
    assert Node (Leaf(1), Leaf(), 3).postorder() == [1, 3]
    assert Node (Leaf(), Leaf(2), 3).postorder() == [2, 3]
    assert Node (Leaf(), Leaf(2), ).postorder() == [2]
    
def test_preorder():
    assert Node (Leaf(1), Leaf(2), 3).postorder() == [3, 1, 2]
    assert Node (Leaf(1), Leaf(2)).postorder() == [1,2]
    assert Node (Leaf(1), Leaf(2)).postorder() == [1,2]
    assert Node (Leaf(), Leaf(), 3).postorder() == [3]
    assert Node (Leaf(1), Leaf(), 3).postorder() == [3, 1]
    assert Node (Leaf(), Leaf(2), 3).postorder() == [3, 2]
    assert Node (Leaf(), Leaf(2), ).postorder() == [2]
######################################################################
