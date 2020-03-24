============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_vigenere _________________________________

    def test_vigenere():
        v1 = Vigenere("MYSECRETKEY")
>       assert v1.decrypt(v1.encrypt("TESTFOOBAR")) == "TESTFOOBAR"

/private/tmp/blabla.py:45: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <blabla.Vigenere object at 0x10491ee10>, w = 'TESTFOOBAR'

    def encrypt(self, w: str) -> str:
        """
        Encrypt the given text with the secret key of the object.
        """
        new_key = self.key * (len(w) // len(self.key) + 1)
        msg = ""
        for i, c in enumerate(w):
>           new_c = chr(ord(c) + (new_key[i] - ord('A')))
E           TypeError: unsupported operand type(s) for -: 'str' and 'int'

/private/tmp/blabla.py:23: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_vigenere - TypeError: unsupported operand ty...
============================== 1 failed in 0.06s ===============================
