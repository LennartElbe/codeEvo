============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        k = "Aallo"
>       print(k[0] + 1)
E       TypeError: can only concatenate str (not "int") to str

/private/tmp/blabla.py:20: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - TypeError: can only concatenate s...
============================== 1 failed in 0.05s ===============================
