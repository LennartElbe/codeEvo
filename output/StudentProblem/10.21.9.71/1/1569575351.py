============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
        print(nwords("  hallo   k  l"))
        k = " lll"
        assert nwords("  ") == 0
        #assert nwords("  hallo   k  l") == 3
>       assert k[0] == string.whitespace
E       AssertionError: assert ' ' == ' \t\n\r\x0b\x0c'
E         Strings contain only whitespace, escaping them using repr()
E         - ' \t\n\r\x0b\x0c'
E         + ' '

/private/tmp/blabla.py:23: AssertionError
----------------------------- Captured stdout call -----------------------------
0
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - AssertionError: assert ' ' == ' \t\...
============================== 1 failed in 0.06s ===============================
