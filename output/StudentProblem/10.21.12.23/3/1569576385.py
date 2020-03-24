============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 3 items

../../../../../tmp FFF                                                   [100%]

=================================== FAILURES ===================================
____________________________________ test_4 ____________________________________

    def test_4():
>       assert leap(1200) == True
E       assert None == True
E        +  where None = leap(2000)

/private/tmp/blabla.py:22: AssertionError
____________________________________ test_5 ____________________________________

    def test_5():
        # Test fr nicht durch 4 teilbar
>       assert leap(2001) == False
E       assert None == False
E        +  where None = leap(2001)

/private/tmp/blabla.py:26: AssertionError
____________________________________ test_6 ____________________________________

    def test_6():
        #Test fr Teilbar durch 100 aber nicht durch 400
>       assert leap(2100) == False
E       assert None == False
E        +  where None = leap(2100)

/private/tmp/blabla.py:30: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_4 - assert None == True
FAILED ../../../../../tmp/::test_5 - assert None == False
FAILED ../../../../../tmp/::test_6 - assert None == False
============================== 3 failed in 0.14s ===============================
