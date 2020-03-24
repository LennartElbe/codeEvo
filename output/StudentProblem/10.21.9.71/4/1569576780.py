============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        k = "Aallo"
        print(str(ord(k[0]) + 1))
>       assert 1 == 0
E       assert 1 == 0

/private/tmp/blabla.py:21: AssertionError
----------------------------- Captured stdout call -----------------------------
66
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - assert 1 == 0
============================== 1 failed in 0.05s ===============================
