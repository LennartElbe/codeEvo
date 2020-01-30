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

class Leaf:
    def __init__(self, value):
        super().__init__(self, value)
        
        def preorder(node):
            li = []
            if node is not None:
                li = li + [node.value] #mark fist
                preorder(node.left) #left second
                preorder(node.right) #right third
        def postorder(node):
            if node is not None:
                preorder(node.left) # left fist
                preorder(node.right) # second third
                li = li + [node.value] # mark third
