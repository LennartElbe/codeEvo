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

class leaf(Leaf0):
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

        
            
