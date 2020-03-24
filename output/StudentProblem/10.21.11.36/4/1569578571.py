============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        t = Vigenere("A")
        assert t.encrypt("HELLO") == "HELLO"
        t2 = Vigenere("B")
>       assert t.encrypt("HELLO") == "IFMMP"
E       AssertionError: assert 'HELLO' == 'IFMMP'
E         - IFMMP
E         + HELLO

/private/tmp/blabla.py:75: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - AssertionError: assert 'HELLO' ==...
============================== 1 failed in 0.06s ===============================
