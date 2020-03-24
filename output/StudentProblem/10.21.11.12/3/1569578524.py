============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert leap(1400) == "1400 ist kein Schaltjahr"
E       AssertionError: assert '1400ist kein Schaltjahr' == '1400 ist kein Schaltjahr'
E         - 1400 ist kein Schaltjahr
E         ?     -
E         + 1400ist kein Schaltjahr

/private/tmp/blabla.py:23: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: assert '1400ist kein ...
============================== 1 failed in 0.05s ===============================
