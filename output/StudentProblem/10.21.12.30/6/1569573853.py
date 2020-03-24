============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        xs1 = [1, 0, 2, 3, -1, -5]
        xs2 = [1, 5, 2, 3, 99, 2.5, 3.5]
>       assert list_filter(0, xs1) == [0, -1, -5], "Fall x=0"
E       AssertionError: Fall x=0
E       assert [] == [0, -1, -5]
E         Right contains 3 more items, first extra item: 0
E         Use -v to get the full diff

/private/tmp/blabla.py:34: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - AssertionError: Fall x=0
============================== 1 failed in 0.05s ===============================
