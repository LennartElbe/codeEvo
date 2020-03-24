============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_filter __________________________________

    def test_filter():
>       assert list_filter(2,[1,2,3]) == [2,3]
E       assert [2] == [2, 3]
E         Right contains one more item: 3
E         Use -v to get the full diff

/private/tmp/blabla.py:23: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_filter - assert [2] == [2, 3]
============================== 1 failed in 0.06s ===============================
