============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert leap(1400) == "1400 ist kein Schaltjahr"
E       AssertionError: assert None == '1400 ist kein Schaltjahr'
E        +  where None = leap(1400)

/private/tmp/blabla.py:23: AssertionError
----------------------------- Captured stdout call -----------------------------
x ist kein Schaltjahr
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: assert None == '1400 ...
============================== 1 failed in 0.06s ===============================
