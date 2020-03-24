============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_tree ___________________________________

    def test_tree():
>       assert Leaf.preorder
E       AttributeError: 'function' object has no attribute 'preorder'

/private/tmp/blabla.py:67: AttributeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_tree - AttributeError: 'function' object has...
============================== 1 failed in 0.06s ===============================
