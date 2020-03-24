============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert leap(2001) == "Schaltjahr" # kein Schaltjahr
E       AssertionError: assert 'False' == 'kein Schaltjahr'
E         - kein Schaltjahr
E         + False

/private/tmp/blabla.py:24: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: assert 'False' == 'ke...
============================== 1 failed in 0.06s ===============================
