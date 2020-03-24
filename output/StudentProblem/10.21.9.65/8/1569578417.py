============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_Node ___________________________________

    def test_Node():
>       n = Node((Leaf(1), Leaf(2), 3))
E       TypeError: __init__() missing 2 required positional arguments: 'right' and 'value'

/private/tmp/blabla.py:52: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Node - TypeError: __init__() missing 2 requi...
============================== 1 failed in 0.04s ===============================
