============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
        assert leap(1200) == None
        assert leap(1600) == True
        assert leap(1604) == True
>       assert leap(1800) == True
E       assert False == True
E        +  where False = leap(1800)

/private/tmp/blabla.py:29: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - assert False == True
============================== 1 failed in 0.06s ===============================
