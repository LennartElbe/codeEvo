============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
        assert leap(2000)==True
        assert leap(1996)==True
>       assert leap(1582)=='please enter a year >1582'
E       AssertionError: assert None == 'please enter a year >1582'
E        +  where None = leap(1582)

/private/tmp/blabla.py:26: AssertionError
----------------------------- Captured stdout call -----------------------------
please enter a year  >1582
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: assert None == 'pleas...
============================== 1 failed in 0.05s ===============================
