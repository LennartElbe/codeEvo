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
    lst = []
    def postorder():
        if leaf is None:
            pass
        else:
            postorder(Node.left)
            postorder(Node.right)
            lst.append(value)
        return lst

    def preorder():
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
    def postorder():
        if leaf is None:
            pass
        else:
            postorder(Node.left)
            postorder(Node.right)
            lst.append(value)
        return lst

    def preorder():
        lst = []
        if leaf is None:
            pass
        else:
            lst.append(value)
            postorder(Node.left)
            postorder(Node.right)
        return lst        
