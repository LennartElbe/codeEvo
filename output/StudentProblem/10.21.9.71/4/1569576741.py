============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        k = "Aallo"
>       print(ord(A))
E       NameError: name 'A' is not defined

/private/tmp/blabla.py:20: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - NameError: name 'A' is not defined
============================== 1 failed in 0.04s ===============================
