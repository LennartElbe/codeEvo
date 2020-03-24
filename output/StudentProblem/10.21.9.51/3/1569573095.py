============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_schaltjahr ________________________________

    def test_schaltjahr():
>       assert(schaltjahr(1582)) == True
E       assert False == True
E        +  where False = schaltjahr(1582)

/private/tmp/blabla.py:24: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_schaltjahr - assert False == True
============================== 1 failed in 0.06s ===============================
