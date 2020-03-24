============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        test = Vigenere("HELLO")
        assert test.encrypt("AAAAA") == "HELLO"
        test = Vigenere("ABC")
>       assert test.entrypt("HELLO") == True
E       AttributeError: 'Vigenere' object has no attribute 'entrypt'

/private/tmp/blabla.py:70: AttributeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - AttributeError: 'Vigenere' object...
============================== 1 failed in 0.05s ===============================
