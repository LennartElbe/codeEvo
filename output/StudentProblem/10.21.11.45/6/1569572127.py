============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert list_filter(2 ,[0,1,2,5,8])
E       assert []
E        +  where [] = list_filter(2, [0, 1, 2, 5, 8])

/private/tmp/blabla.py:22: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - assert []
============================== 1 failed in 0.05s ===============================
