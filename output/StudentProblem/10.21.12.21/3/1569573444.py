============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert leap(2004) == '2004 ist ein Schaltjahr', True
E       AssertionError: True
E       assert True == '2004 ist ein Schaltjahr'
E        +  where True = leap(2004)

/private/tmp/blabla.py:46: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: True
============================== 1 failed in 0.06s ===============================
