============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_tree ___________________________________

    def test_tree():
>       assert Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
E       assert [3] == [1, 2, 3]
E         At index 0 diff: 3 != 1
E         Right contains 2 more items, first extra item: 2
E         Use -v to get the full diff

/private/tmp/blabla.py:67: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_tree - assert [3] == [1, 2, 3]
============================== 1 failed in 0.06s ===============================
