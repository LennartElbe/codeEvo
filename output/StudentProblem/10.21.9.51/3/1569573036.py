============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_schaltjahr ________________________________

    def test_schaltjahr():
        assert(schaltjahr(1582)) == True
        assert(schaltjahr(2006)) == True
>       assert(schaltjahr(2005)) == False
E       assert True == False
E        +  where True = schaltjahr(2005)

/private/tmp/blabla.py:25: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_schaltjahr - assert True == False
============================== 1 failed in 0.06s ===============================
