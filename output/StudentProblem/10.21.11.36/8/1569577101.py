============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_preorder _________________________________

    def test_preorder():
        t1 = Node(Leaf(None), Leaf(None), None)
        assert t1.postorder() == []
        t2 = Node(Leaf(1), Leaf(2), 3)
        assert t2.postorder() == [1, 2, 3]
        t3 = Node(Leaf(1), Leaf(2), None)
        assert t3.postorder() == [1, 2]
        t4 = Leaf(1)
        assert t4.postorder() == [1]
        t5 = Leaf(None)
        assert t5.postorder() == []
        t6 = Node(Node(Leaf(1), Leaf(2), 3), Node(Leaf(4), Leaf(5), 6), 7)
>       assert t6.postorder() == [1, 2, 3, 7, 4, 5, 6]
E       assert [3, 1, 2, 6, 4, 5, ...] == [1, 2, 3, 7, 4, 5, ...]
E         At index 0 diff: 3 != 1
E         Use -v to get the full diff

/private/tmp/blabla.py:124: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_preorder - assert [3, 1, 2, 6, 4, 5, ...] ==...
============================== 1 failed in 0.07s ===============================
