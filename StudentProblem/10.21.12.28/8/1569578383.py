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

def peroder(Node0):
    if Node0 is None:
        return None
    else:
        perpder(self.value)
        perpder(self.left)
        perpder(self.right)

        
def postorder(Node0):
    if Node0 is None:
        return None
    else:
        postorder(self.left)
        postorder(self.right)
        postorder(self.value)
