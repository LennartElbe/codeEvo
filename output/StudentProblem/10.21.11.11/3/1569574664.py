============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
        assert leap(1582) == False
        assert leap(1583) == False
>       assert leap(1600) == True
E       assert None == True
E        +  where None = leap(1600)

/private/tmp/blabla.py:29: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - assert None == True
============================== 1 failed in 0.05s ===============================
