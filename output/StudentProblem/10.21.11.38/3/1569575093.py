============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
        """this function tests leap()"""
        assert leap(2000) == True
>       assert leap(2100) == False
E       assert True == False
E        +  where True = leap(2100)

/private/tmp/blabla.py:22: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - assert True == False
============================== 1 failed in 0.06s ===============================
