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

/private/tmp/blabla.py:69: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <blabla.Vigenere object at 0x10c38ca50>, w = 'HELLO'

    def encrypt(self, w: str) -> str:
        w_len = len(w)
        keylen = len(self.key)
        keyword = ""
        encrypted = ""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if keylen < w_len:
>           keyword = self.key * (w_len // keylen) + 1
E           TypeError: can only concatenate str (not "int") to str

/private/tmp/blabla.py:22: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - TypeError: can only concatenate s...
============================== 1 failed in 0.05s ===============================
