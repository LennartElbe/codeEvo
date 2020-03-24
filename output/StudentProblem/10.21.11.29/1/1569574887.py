============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
        assert(nwords("Ha Ho H") == 2)
>       assert(nwords("HALLOHALLOHALLO") == 1)
E       AssertionError: assert 14 == 1
E        +  where 14 = nwords('HALLOHALLOHALLO')

/private/tmp/blabla.py:25: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - AssertionError: assert 14 == 1
============================== 1 failed in 0.04s ===============================
