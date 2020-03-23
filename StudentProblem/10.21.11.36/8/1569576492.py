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
# Pre-Order (Hauptreihenfolge): Zuerst der Knoten selbst,dann der linke, danach der rechte Teilbaum
# Post-Order (Nebenreihenfolge): Zuerst der linke, danachder rechte Teilbaum, zum Schluss der Knoten selbst

class Node(Node0):
    def preorder(self):
        """Preorder traversing
        """
        if self.value is not None:
            vals = [self.value]
        else:
            vals = []
        if self.left is None and self.right is None:
            pass
        elif self.left is None:
            vals += self.right.preorder()    
        elif self.right is None:
            vals += self.left.preorder()
        else:
            vals += self.left.preorder()
            vals += self.right.preorder() 
        return vals
    def postorder(self):
        """Postorder traversing
        """
        vals = []
        if self.left is None and self.right is None:
            pass
        elif self.left is None:
            vals += self.right.preorder()    
        elif self.right is None:
            vals += self.left.preorder()
        else:
            vals += self.left.preorder()
            vals += self.right.preorder() 
        if self.value is not None:
            vals += self.value
        return vals
        
class Leaf(Leaf0):
    """Class for a leaf of a binary tree with methods pre-order and post-order
    """
    def preorder(self):
        """Preorder traversing
        """
        if self.value is not None:
            return [self.value]
        else:
            return []
    
    def posstorder(self):
        """Preorder traversing
        """
        if self.value is not None:
            return [self.value]
        else:
            return []


        
    

print(Node (Leaf(1), Leaf(2)).preorder())
print(Node (Leaf(1), Leaf(2), 3).preorder())
print(Node (Leaf(1), Leaf(2)).postorder())
print(Node (Leaf(1), Leaf(2), 3).postorder())
######################################################################
## Lösung Teil 2.

######################################################################
