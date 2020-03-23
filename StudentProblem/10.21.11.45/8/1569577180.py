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
    def __init__(self,value):
        self.value = value
    def postorder(tree):
        if tree is None:
            pass
        else:
            post.order(tree.left)
            post.order(tree.right)
            post.order(tree.mark)
    def preorder(tree):
        if tree is None:
            pass
        else:
            pre.order(tree.mark)
            pre.order(tree.left)
            pre.order(tree.right)

class Node(Node0):
    def __init__(self, left, right, value = None):
        self.left = left
        self.right = right
        self.value = value
    def postorder(tree):
        if tree is None:
            pass
        else:
            post.order(tree.left)
            post.order(tree.right)
            post.order(tree.mark)
    def preorder(tree):
        if tree is None:
            pass
        else:
            pre.order(tree.mark)
            pre.order(tree.left)
            pre.order(tree.right)

        
            
######################################################################
## Lösung Teil 2.
Node(Leaf(3), Leaf(4), 5).post.order() == [3, 4, 5]
Node(Leaf(3), Leaf(4)).postorder() == [3, 4]

Node(Leaf(3), Leaf(4), 5).preorder() == [5,3,4]
Node(Leaf(3), Leaf(4)).preorder() == [3, 4]
######################################################################
