============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
        assert leap(2000)
>       assert leap(2001)
E       assert False
E        +  where False = leap(2001)

/private/tmp/blabla.py:17: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - assert False
============================== 1 failed in 0.05s ===============================
