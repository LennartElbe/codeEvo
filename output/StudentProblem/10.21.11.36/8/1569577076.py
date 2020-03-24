============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_preorder _________________________________

    def test_preorder():
        t1 = Node(Leaf(None), Leaf(None), None)
        assert t1.preorder() == []
        t2 = Node(Leaf(1), Leaf(2), 3)
>       assert t2.preorder() == [1, 2, 3]
E       assert [3, 1, 2] == [1, 2, 3]
E         At index 0 diff: 3 != 1
E         Use -v to get the full diff

/private/tmp/blabla.py:116: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_preorder - assert [3, 1, 2] == [1, 2, 3]
============================== 1 failed in 0.06s ===============================
