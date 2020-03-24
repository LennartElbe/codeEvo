============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 3 items

../../../../../tmp .F.                                                   [100%]

=================================== FAILURES ===================================
____________________________________ test_5 ____________________________________

    def test_5():
        # Test fr nicht durch 4 teilbar
>       assert leap(2001) == False
E       assert True == False
E        +  where True = leap(2001)

/private/tmp/blabla.py:31: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_5 - assert True == False
========================= 1 failed, 2 passed in 0.05s ==========================
