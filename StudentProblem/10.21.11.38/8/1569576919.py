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
class Node(Node0):
    """Node and Leaf are subclasses of Node0 and Leaf0"""
    def __init__(self, left, right, mark, value = None):
        self.left = left
        self.right = right
        self.mark = mark
        self.value = value

class Leaf(Leaf0):
    def __init___(self, value):
        self.value = value
    
    def preorder(Node):
        """returns preorder print of a tree
        args: node
        returns: preorder print of a tree"""
        if Leaf == None:
            return None
        res = []
        preorder(Node.mark):
            append.res(mark.value) if value != None
        preorder(Node.left):
            append.res(left.value) if value != None
        preorder(Node.right):
            append.res(right.value) if value != None

    def postorder(Node):
        """returns postorder print of a tree
        args: Node
        res: postorder print"""
        res = []
        postorder(Node.left):
            append.res(mark.value) if value != None
        postorder(Node.right):
            append.res(right.value) if value != None
        postorder(Node.mark):
            append.res(mark.value) if value != None
        return res    
        
        
        
######################################################################
## Lösung Teil 2.

######################################################################
