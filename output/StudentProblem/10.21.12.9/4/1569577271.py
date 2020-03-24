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
        assert test.encrypt("HELLO") == "HFNLP"
>       assert test.decrypt("HFNLP") == "HELLO"

/private/tmp/blabla.py:71: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <blabla.Vigenere object at 0x10b4abe90>, w = 'HFNLP'

    def decrypt(self, w):
        w_len = len(w)
        keylen = len(self.key)
        keyword = ""
        decrypted = ""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if keylen < w_len:
>           keyword = self.key * (w_len // keylen) + 1
E           TypeError: can only concatenate str (not "int") to str

/private/tmp/blabla.py:45: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - TypeError: can only concatenate s...
============================== 1 failed in 0.05s ===============================
