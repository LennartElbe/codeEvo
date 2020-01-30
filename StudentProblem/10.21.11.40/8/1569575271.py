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

def Leaf(Leaf0):
    def __init__(self, *args):
        super(self, *args)
        
    def preorder(self) -> list:
        """
        Returns a list of the leaf in preorder without any None values.
        """
        return self.value
    
    def postorder(self) -> list:
        """
        Returns a list of the leaf in postorder without any None values.
        """
        return self.value

class Node(Node0):
    def __init__(self, *args):
        super(self, *args)
       
    def preorder(self) -> list:
        """
        Returns a list of the node in preorder without any None values.
        """
        ls = []
        if self.value:
            ls += self.value
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
            ls += self.value
        return ls
