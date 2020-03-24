============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        test = Vigenere("ABC")
>       assert test.encrypt("HELLO") == "HGOLQ"
E       AssertionError: assert 'HFNLP' == 'HGOLQ'
E         - HGOLQ
E         + HFNLP

/private/tmp/blabla.py:68: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - AssertionError: assert 'HFNLP' ==...
============================== 1 failed in 0.05s ===============================
