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
class leaf0():
    def __init__(self,value):
        self.value =value
class Node():
    def __init__(self,left,right,value=None):
        self.value=value
        self.left =left
        self.right =right
    def postorder(self):
        if True:
            self.left()
            self.right()
            print(self.value())
        else:
            return []
    def preorder(self):
        if True:
            print(self.value)
            self.left()
            self.right()
        else:
            return []
            
        
      
        
######################################################################
## Lösung Teil 2.

######################################################################
