============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_Node ___________________________________

    def test_Node():
        n = Node(Leaf(1), Leaf(2), 3)
>       n.perorder() == [3, 1, 2]

/private/tmp/blabla.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <blabla.Node object at 0x105760750>

    def perorder(self):
        res = []
        if self.value is None:
            pass
        else:
            res += [self.value]
>           self.preorder(self.left)
E           AttributeError: 'Node' object has no attribute 'preorder'

/private/tmp/blabla.py:34: AttributeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Node - AttributeError: 'Node' object has no ...
============================== 1 failed in 0.05s ===============================
