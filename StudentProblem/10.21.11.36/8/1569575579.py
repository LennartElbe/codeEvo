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

class Leaf(Leaf0):
    """Class for a leaf of a binary tree
    """
    

class Node(Node0):
    
    
a = Node(1, 2, 3)
print(a.left)
######################################################################
## Lösung Teil 2.

######################################################################
