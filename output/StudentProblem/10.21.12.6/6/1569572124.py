============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        """
        """
        testlist1 = [1, 2, 3, 4, 5, 6]
        testlist2 = [3, 4, 5, 6, 7, 8]
>       assert list_filter(3, testlist1) == [1, 2, 3]
E       assert [3, 3, 3] == [1, 2, 3]
E         At index 0 diff: 3 != 1
E         Use -v to get the full diff

/private/tmp/blabla.py:31: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - assert [3, 3, 3] == [1, 2, 3]
============================== 1 failed in 0.05s ===============================
