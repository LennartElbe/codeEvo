============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert list_filter(5,[5,9]) == [5]
E       assert [] == [5]
E         Right contains one more item: 5
E         Use -v to get the full diff

/private/tmp/blabla.py:18: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - assert [] == [5]
============================== 1 failed in 0.05s ===============================
