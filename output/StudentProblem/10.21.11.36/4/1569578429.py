============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_Vigenere _________________________________

    def test_Vigenere():
        t = Vigenere("A")
        assert t.encrypt("Hello") == "Hello"
>       assert t.decrypt("Hello") == "Hello"
E       AssertionError: assert None == 'Hello'
E        +  where None = <bound method Vigenere.decrypt of <blabla.Vigenere object at 0x10d8e7ad0>>('Hello')
E        +    where <bound method Vigenere.decrypt of <blabla.Vigenere object at 0x10d8e7ad0>> = <blabla.Vigenere object at 0x10d8e7ad0>.decrypt

/private/tmp/blabla.py:69: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_Vigenere - AssertionError: assert None == 'H...
============================== 1 failed in 0.06s ===============================
