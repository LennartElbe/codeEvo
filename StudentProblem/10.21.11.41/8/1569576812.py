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
        self.value = value
    

class Node:
    def __init__(self, left, right, value):
        self.value = value
        self.left = left
        self.right = right
    
    def preorder(self):   #knoten, links, rechts
        if self.value == None and self.left == None and self.right == None:
            return []
        elif self.left == None and self.right == None:
            return [self.value]
        else:
            return list(self.value, self.left.preorder(), self.right.preorder())
    
    def postorder(self):    #links, rechts, knoten
        if self.value == None and self.left == None and self.right == None:
            return []
        elif self.left == None and self.right == None:
            return [self.value]
        else:
            return list(self.left.postorder(), self.right.postorder(), self.value)
          
               