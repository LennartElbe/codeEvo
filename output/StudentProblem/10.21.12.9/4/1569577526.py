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
        assert test.decrypt("WORLD") == "E@R@2"
        assert test.encrypt("E@R@2") == "WORLD"
        test = Vigenere("HAM")
        assert test.encrypt("") == ""
>       assert test.encrypt("LEHMANN") == True
E       AssertionError: assert 'SETTAZU' == True
E        +  where 'SETTAZU' = <bound method Vigenere.encrypt of <blabla.Vigenere object at 0x1039dded0>>('LEHMANN')
E        +    where <bound method Vigenere.encrypt of <blabla.Vigenere object at 0x1039dded0>> = <blabla.Vigenere object at 0x1039dded0>.encrypt

/private/tmp/blabla.py:77: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - AssertionError: assert 'SETTAZU' ...
============================== 1 failed in 0.06s ===============================
