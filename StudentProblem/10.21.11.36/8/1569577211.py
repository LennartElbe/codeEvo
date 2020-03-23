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
    """Class for a node of a binary tree.
    Attributes:
        value: value of the node
        left: left child (Node or Leaf)
        right: right child(Node or Leaf)
    Methods for preorder and postorder traversing    
    """
    def preorder(self):
        """Preorder traversing
        Returns: 
            list: all values in the tree that are not None
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
        Returns: 
            list: all values in the tree that are not None
        """
        vals = []
        if self.left is None and self.right is None:
            pass
        elif self.left is None:
            vals += self.right.postorder()    
        elif self.right is None:
            vals += self.left.postorder()
        else:
            vals += self.left.postorder()
            vals += self.right.postorder() 
        if self.value is not None:
            vals += [self.value]
        return vals
        
class Leaf(Leaf0):
    """Class for a leaf of a binary tree with methods pre-order and post-order.
    Attributes:
        Value: The value of the leaf node
    Methods:
        Preorder and Postorder traversing that return the value of the leaves
        if they are not None. 
    """
    def preorder(self):
        """Preorder traversing
        """
        if self.value is not None:
            return [self.value]
        else:
            return []
    
    def postorder(self):
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
print(Node(Node(Leaf(1), Leaf(2), 3), Node(Leaf(4), Leaf(5), 6), 7).postorder())
######################################################################
## Lösung Teil 2.
def test_preorder():
    t1 = Node(Leaf(None), Leaf(None), None)
    assert t1.preorder() == []
    t2 = Node(Leaf(1), Leaf(2), 3)
    assert t2.preorder() == [3, 1, 2]
    t3 = Node(Leaf(1), Leaf(2), None)
    assert t3.preorder() == [1, 2]
    t4 = Leaf(1)
    assert t4.preorder() == [1]
    t5 = Leaf(None)
    assert t5.preorder() == []
    t6 = Node(Node(Leaf(1), Leaf(2), 3), Node(Leaf(4), Leaf(5), 6), 7)
    assert t6.preorder() == [7, 3, 1, 2, 6, 4, 5]

def test_preorder():
    t1 = Node(Leaf(None), Leaf(None), None)
    assert t1.postorder() == []
    t2 = Node(Leaf(1), Leaf(2), 3)
    assert t2.postorder() == [1, 2, 3]
    t3 = Node(Leaf(1), Leaf(2), None)
    assert t3.postorder() == [1, 2]
    t4 = Leaf(1)
    assert t4.postorder() == [1]
    t5 = Leaf(None)
    assert t5.postorder() == []
    t6 = Node(Node(Leaf(1), Leaf(2), 3), Node(Leaf(4), Leaf(5), 6), 7)
    assert t6.postorder() == [1, 2, 3, 4, 5, 6, 7]
######################################################################
