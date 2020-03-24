============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
        assert list_filter(5,[1,1,3,5,9]) == [1,1,3,5]
        assert list_filter(15, [1,5,3,8,14,18,20,6]) == [1,5,3,8,14,6]
>       assert list_filter(20, [4,6,8,5,7,0]) == []
E       assert [4, 6, 8, 5, 7, 0] == []
E         Left contains 6 more items, first extra item: 4
E         Use -v to get the full diff

/private/tmp/blabla.py:24: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - assert [4, 6, 8, 5, 7, 0] == []
============================== 1 failed in 0.05s ===============================
