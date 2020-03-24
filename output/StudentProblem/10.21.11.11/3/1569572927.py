============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert leap(1582) == 'oh no'
E       AssertionError: assert None == 'oh no'
E        +  where None = leap(1582)

/private/tmp/blabla.py:16: AssertionError
----------------------------- Captured stdout call -----------------------------
oh no
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: assert None == 'oh no'
============================== 1 failed in 0.05s ===============================
