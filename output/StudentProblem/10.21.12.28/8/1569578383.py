============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test_1 ____________________________________

    def test_1():
>       assert Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
E       NameError: name 'Leaf' is not defined

/private/tmp/blabla.py:38: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_1 - NameError: name 'Leaf' is not defined
============================== 1 failed in 0.06s ===============================
