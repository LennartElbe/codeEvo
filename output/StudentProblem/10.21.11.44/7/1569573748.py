============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(6) == [6,3, 2, 1] #normal
E       assert False == [6, 3, 2, 1]
E        +  where False = divisors(6)

/private/tmp/blabla.py:22: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert False == [6, 3, 2, 1]
============================== 1 failed in 0.04s ===============================
