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
E       AssertionError: assert 0 == 3
E        +  where 0 = nwords('  ')

/private/tmp/blabla.py:20: AssertionError
----------------------------- Captured stdout call -----------------------------
0
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - AssertionError: assert 0 == 3
============================== 1 failed in 0.05s ===============================
