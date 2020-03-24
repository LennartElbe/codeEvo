============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_vigenere _________________________________

    def test_vigenere():
        v1 = Vigenere("MYSECRETKEY")
        assert v1.decrypt(v1.encrypt("TESTFOOBAR")) == "TESTFOOBAR"
    
        v2 = Vigenere("AAA")
        assert v2.encrypt("BBB") == "BBB"
    
>       assert Vigenere("ABCD").encrypt("BAR") == "BBU"
E       AssertionError: assert 'BBT' == 'BBU'
E         - BBU
E         + BBT

/private/tmp/blabla.py:50: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_vigenere - AssertionError: assert 'BBT' == '...
============================== 1 failed in 0.07s ===============================
