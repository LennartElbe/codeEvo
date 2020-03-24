============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_tree ___________________________________

    def test_tree():
        assert Node(Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]
        assert Node(Leaf(1), Leaf(2), 3).preorder() == [3, 1, 2]
    
        assert Node(Node(None, Leaf(10), None), Leaf(2), 3).postorder() == [10, 2, 3]
>       assert Node(Node(None, Leaf(10), None), Leaf(2), 3).preorder() == [2, 3, 10]
E       assert [3, 10, 2] == [2, 3, 10]
E         At index 0 diff: 3 != 2
E         Use -v to get the full diff

/private/tmp/blabla.py:71: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_tree - assert [3, 10, 2] == [2, 3, 10]
============================== 1 failed in 0.07s ===============================
