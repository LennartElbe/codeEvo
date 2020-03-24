============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
        assert leap (1500) == False
        assert leap (2000) == True
        assert leap (2100) == False
        assert leap (1600) == True
>       assert leap (1720) == False
E       assert True == False
E        +  where True = leap(1720)

/private/tmp/blabla.py:27: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - assert True == False
============================== 1 failed in 0.06s ===============================
