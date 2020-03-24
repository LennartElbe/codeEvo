============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        assert list_filter(5, [1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5]
        assert list_filter(0, [1, 2, 3, 4, 5, 6, 7]) == []
        assert list_filter(0, []) == []
        assert list_filter(7, []) == []
>       assert list_filter(0, [5, 15, 37, 1, 0]) == [5, 15, 37, 1, 0]
E       assert [0] == [5, 15, 37, 1, 0]
E         At index 0 diff: 0 != 5
E         Right contains 4 more items, first extra item: 15
E         Use -v to get the full diff

/private/tmp/blabla.py:25: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - assert [0] == [5, 15, 37, 1, 0]
============================== 1 failed in 0.06s ===============================
