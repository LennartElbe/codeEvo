============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 3 items

../../../../../tmp .FF                                                   [100%]

=================================== FAILURES ===================================
____________________________________ test_5 ____________________________________

    def test_5():
        # Test fr nicht durch 4 teilbar
>       assert leap(2001) == False
E       assert True == False
E        +  where True = leap(2001)

/private/tmp/blabla.py:31: AssertionError
____________________________________ test_6 ____________________________________

    def test_6():
        #Test fr Teilbar durch 100 aber nicht durch 400
>       assert leap(2000) == False
E       assert True == False
E        +  where True = leap(2000)

/private/tmp/blabla.py:35: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_5 - assert True == False
FAILED ../../../../../tmp/::test_6 - assert True == False
========================= 2 failed, 1 passed in 0.06s ==========================
