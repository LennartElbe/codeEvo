============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
        assert(leap(2006) == False)
>       assert(leap(2007) == True)
E       assert False == True
E        +  where False = leap(2007)

/private/tmp/blabla.py:29: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - assert False == True
============================== 1 failed in 0.04s ===============================
