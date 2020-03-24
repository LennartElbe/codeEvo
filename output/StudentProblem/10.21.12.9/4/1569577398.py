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
        assert test.decrypt("HFNLP") == "HELLO"
        test = Vigenere("SPAM")
>       assert test.decrypt("WORLD") == True
E       AssertionError: assert 'E@R@2' == True
E        +  where 'E@R@2' = <bound method Vigenere.decrypt of <blabla.Vigenere object at 0x10e4f6a50>>('WORLD')
E        +    where <bound method Vigenere.decrypt of <blabla.Vigenere object at 0x10e4f6a50>> = <blabla.Vigenere object at 0x10e4f6a50>.decrypt

/private/tmp/blabla.py:73: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - AssertionError: assert 'E@R@2' ==...
============================== 1 failed in 0.06s ===============================
