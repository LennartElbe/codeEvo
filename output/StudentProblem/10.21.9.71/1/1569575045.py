============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
>       assert nword("  ") == 0
E       NameError: name 'nword' is not defined

/private/tmp/blabla.py:18: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - NameError: name 'nword' is not defined
============================== 1 failed in 0.05s ===============================
