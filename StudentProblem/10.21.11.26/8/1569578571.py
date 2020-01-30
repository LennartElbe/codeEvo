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

class Leaf(Leaf0, Node0):
    """A lower-class leaf of class Leaf0"""
    def __init__(self, value):
        super().value = value
        
    def postorder(tree):
        """method to output your tree in postorder
        
        Args:
            tree(leaf): a tree of class leaf
        Return:
            None
        """
        if tree.value != None:
            print(tree.value)
            
    def preorder(tree):
        """method to output your tree in preorder
        
        Args:
            tree(leaf): a tree of class leaft
            
        Return:
            None
        """
        if tree is None:
            pass
        else:
            print(tree.value)
            preorder(tree.left)
            preorder(tree.right)
            
class Node(Node0):                      # Vererbung
    """A class Node"""
    def __init__(self, left, right, value):
        super().left = left
        super().right = right
        super().value = value
    
    def preorder(tree):
        """method to output your tree in preorder
        
        Args:
            tree(leaf): a tree of class leaft
            
        Return:
            None
        """
        if tree is None:
            pass
        else:
            print(tree.value)
            preorder(tree.left)
            preorder(tree.right)
        
        def postorder(tree):
        """method to output your tree in preorder
        
        Args:
            tree(leaf): a tree of class leaft
            
        Return:
            None"""
        if tree is None:
            pass
        else:
            preorder(tree.left)
            preorder(tree.right)
            print(tree.value)
