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
class Node:
    """Subclass to the class Node0"""
    def __init__(self, mark, **kwargs):
        self.mark = mark
        super.**kwargs == kwargs**
    
    def postorder(tree):
        """Computes the preorder of th tree"""
        if tree is None:
            pass
        else:
            postorder(tree.left)
            postorder(tree.right)
            print(tree.mark)
            
    def preorder(tree):
        if tree is None:
            pass
        else:
            print(tree.mark)
            preorder(tree.left)
            preorder(tree.right)
            
class Leaf:
    """Subclass to the class Leaf0"""
   def
        
            
        
######################################################################
## Lösung Teil 2.
assert postorder( Node (Leaf(1), Leaf(2), 3)) == [1,2,3]
assert postorder(Node (Leaf(1), Leaf(2)) == [1,2]
assert preorder(Node(Leaf(1), Leaf(2),3)) == [3,1,2]
assert preorder(Node (Leaf(1), Leaf(2))== [1,2]
assert preorder()== None     
assert postorder() == None
assert postorder(Node (Leaf(1), Leaf(2))== preorder(Node (Leaf(1), Leaf(2))
######################################################################
