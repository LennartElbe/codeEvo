============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
>       assert nwords("  ") == 1
E       AssertionError: assert None == 1
E        +  where None = nwords('  ')

/private/tmp/blabla.py:18: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - AssertionError: assert None == 1
============================== 1 failed in 0.05s ===============================
