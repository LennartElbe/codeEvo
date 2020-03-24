============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
>       assert list_filter(5, ["1","2","3","4","5","6"]) == ["1","2","3","4","5"]
E       AssertionError: assert ['1'] == ['1', '2', '3', '4', '5']
E         Right contains 4 more items, first extra item: '2'
E         Use -v to get the full diff

/private/tmp/blabla.py:23: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - AssertionError: assert ['1'] =...
============================== 1 failed in 0.05s ===============================
