============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp F.                                                    [100%]

=================================== FAILURES ===================================
________________________________ test_preorder _________________________________

    def test_preorder():
        t1 = Node(Leaf(None), Leaf(None), None)
        assert t1.preorder() == []
        t2 = Node(Leaf(1), Leaf(2), 3)
        assert t2.preorder() == [3, 1, 2]
        t3 = Node(Leaf(1), Leaf(2), None)
        assert t3.preorder() == [1, 2]
        t4 = Leaf(1)
>       assert t4.preorder() == [4]
E       assert [1] == [4]
E         At index 0 diff: 1 != 4
E         Use -v to get the full diff

/private/tmp/blabla.py:106: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_preorder - assert [1] == [4]
========================= 1 failed, 1 passed in 0.06s ==========================
