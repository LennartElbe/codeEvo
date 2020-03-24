============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_nwords_a _________________________________

    def test_nwords_a():
        a = "Das ist ein Test"
>       assert nwords(a) == 4
E       AssertionError: assert 1 == 4
E        +  where 1 = nwords('Das ist ein Test')

/private/tmp/blabla.py:16: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords_a - AssertionError: assert 1 == 4
============================== 1 failed in 0.05s ===============================
