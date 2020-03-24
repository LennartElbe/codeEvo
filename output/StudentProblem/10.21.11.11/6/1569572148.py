============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        assert list_filter(0, []) == []
        assert list_filter(1, [0,1,2]) == [0,1]
        assert list_filter(-1,[-2,1]) == [-2]
>       assert list_filter(5,[i for i in range(0,100)]) == [k for k in range(5,100)]
E       assert [0, 1, 2, 3, 4, 5] == [5, 6, 7, 8, 9, 10, ...]
E         At index 0 diff: 0 != 5
E         Right contains 89 more items, first extra item: 11
E         Use -v to get the full diff

/private/tmp/blabla.py:21: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - assert [0, 1, 2, 3, 4, 5] == [...
============================== 1 failed in 0.05s ===============================
