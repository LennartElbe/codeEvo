============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        assert list_filter([3, 2, 7], 4) == [3, 2]
>       assert list_filter([1, 2, 3], 5) == []
E       assert [1, 2, 3] == []
E         Left contains 3 more items, first extra item: 1
E         Use -v to get the full diff

/private/tmp/blabla.py:30: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - assert [1, 2, 3] == []
============================== 1 failed in 0.05s ===============================
