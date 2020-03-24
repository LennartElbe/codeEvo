============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test1 _____________________________________

    def test1():
        a = []
        b = [1,2,3,4,5,6,7]
        c = [0, 2]
        d = [0.2, 0.5, 4.3]
        assert list_filter(20, a) == []
        assert list_filter(-1, b) == []
        assert list_filter(2, c) == [0, 2]
>       assert list_filter(4.31, d) == [4.3]
E       assert [0.2, 0.5, 4.3] == [4.3]
E         At index 0 diff: 0.2 != 4.3
E         Left contains 2 more items, first extra item: 0.5
E         Use -v to get the full diff

/private/tmp/blabla.py:27: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test1 - assert [0.2, 0.5, 4.3] == [4.3]
============================== 1 failed in 0.05s ===============================
