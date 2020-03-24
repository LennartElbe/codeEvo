============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        assert list_filter(0,[]) == [] #empty
        assert list_filter(10,[1,2,3,5]) == [1,2,3,5] #all
>       assert list_filter(5,[6,7,8]) #none
E       assert []
E        +  where [] = list_filter(5, [6, 7, 8])

/private/tmp/blabla.py:20: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - assert []
============================== 1 failed in 0.05s ===============================
