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

self = <blabla.Node object at 0x103e605d0>, args = (None, None, 3)

    def __init__(self, *args):
>       super(self, *args)
E       TypeError: super() takes at most 2 arguments (4 given)

/private/tmp/blabla.py:37: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_tree - TypeError: super() takes at most 2 ar...
============================== 1 failed in 0.06s ===============================
