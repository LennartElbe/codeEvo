============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        Schlssl = Vigenere("AAAABBBB")
>       assert(Vigenere("AAAABBBB").encrypt() == "00001111")
E       AttributeError: 'Vigenere' object has no attribute 'encrypt'

/private/tmp/blabla.py:44: AttributeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - AttributeError: 'Vigenere' object...
============================== 1 failed in 0.05s ===============================
