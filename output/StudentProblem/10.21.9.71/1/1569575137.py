============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
        print(nwords("  "))
>       assert nwords("  ") == 3
E       AssertionError: assert None == 3
E        +  where None = nwords('  ')

/private/tmp/blabla.py:19: AssertionError
----------------------------- Captured stdout call -----------------------------
None
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - AssertionError: assert None == 3
============================== 1 failed in 0.05s ===============================
