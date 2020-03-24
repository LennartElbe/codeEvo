============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_tree ___________________________________

    def test_tree():
>       assert Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]

/private/tmp/blabla.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <blabla.Node object at 0x1095d45d0>

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
>           ls += self.value
E           TypeError: 'int' object is not iterable

/private/tmp/blabla.py:62: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_tree - TypeError: 'int' object is not iterable
============================== 1 failed in 0.06s ===============================
