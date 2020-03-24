============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
>       assert nwords("hello world") == 2
E       AssertionError: assert 'ewrte ert' == 2
E        +  where 'ewrte ert' = nwords('hello world')

/private/tmp/blabla.py:23: AssertionError
----------------------------- Captured stdout call -----------------------------
ewrte ert
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - AssertionError: assert 'ewrte ert' ...
============================== 1 failed in 0.05s ===============================
