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
class Leaf(Leaf0):
    def __init__(self, value):
        self. value = value
    
    def preorder(Leaf):
        if 
        else:
            postorder

class Node(Node0):
    def __init__(self, left, right, value=None):
        self.left = left
        self.right = right
        self.value = value
    def postorder(Node):
        if Node is None:
            pass
        else:
            return[postorder(Node.left), postorder(Node.right), Node.value]
            
def test():
    assert  Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
######################################################################
## hidden code

def mk_coverage():
    covered = set()
    target = set(range(6))
    count = 0
    
    def coverage (func):
        nonlocal covered, target, count

        def wrapper (left, right, value=None):
            nonlocal covered, count
            if value is None:
                covered.add(0)
            else:
                covered.add(1)
            if isinstance (left, Leaf0):
                covered.add(2)
            else:
                covered.add (3)
            if isinstance (right, Leaf0):
                covered.add (4)
            else:
                covered.add (5)
            r = func (left, right, value)
            count += 1
            return r

        if func == "achieved": return len(covered)
        if func == "required": return len(target)
        if func == "count" : return count
        functools.update_wrapper (wrapper, func)    
        return wrapper

    return coverage

coverage = mk_coverage ()
try:
    Node = coverage (Node)
except:
    pass

## Lösung Teil 2.

######################################################################
## hidden tests
pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])

class TestNames:
    def test_Leaf (self):
        assert Leaf
        assert Leaf.preorder
        assert Leaf.postorder
    def test_Node (self):
        assert Node
        assert Node.preorder
        assert Node.postorder

class TestGrades:
   
    def test_coverage(self):
        assert coverage("achieved") == coverage("required")

    def test_Node_is_a_class(self):
        assert "class" in repr (Node.__wrapped__)

    def test_Leaf_is_a_class(self):
        assert "class" in repr (Leaf)

    def test_docstring_classes(self):
        assert Node.__doc__ is not None
        assert Leaf.__doc__ is not None

    def test_docstring_methods(self):
        assert Node.preorder.__doc__ is not None
        assert Node.postorder.__doc__ is not None
        assert Leaf.preorder.__doc__ is not None
        assert Leaf.postorder.__doc__ is not None

    def preorder (self, t):
        if isinstance(t, Leaf0):
            return [t.value]
        if isinstance(t, Node0):
            subtrees = self.preorder (t.left) + self.preorder (t.right)
            return [t.value] + subtrees if t.value else subtrees
        return None

    def postorder (self, t):
        if isinstance(t, Leaf0):
            return [t.value]
        if isinstance(t, Node0):
            subtrees = self.preorder (t.left) + self.preorder (t.right)
            return subtrees + [t.value] if t.value else subtrees
        return None

    def test_0(self):
        t = Leaf (42)
        assert t.postorder() == self.postorder (t)
        assert t.preorder() == self.preorder (t)

    def gen_random_tree (self, n, full=False):
        k = random.randrange (n)
        if k == 0:
            return Leaf (random. randrange (100))
        else:
            tl = self.gen_random_tree (n - 1)
            tr = self.gen_random_tree (n - 1)
            v = random.randrange (-100, -1) if full else None
            return Node (tl, tr, v)
        
    def test_correctness (self):
        for i in range (100):
            t = self.gen_random_tree(5, True)
            assert t.postorder() == self.postorder (t)
            assert t.preorder() == self.preorder (t)

    def test_preorder_postorder(self):
        for i in range (50):
            t = self.gen_random_tree (5)
            assert t.postorder() == t.preorder()


