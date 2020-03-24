============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
        assert(divisors(0)) == []
>       assert(divisors(4)) == [4]

/private/tmp/blabla.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/private/tmp/blabla.py:22: in divisors
    return (divisors(n))
/private/tmp/blabla.py:22: in divisors
    return (divisors(n))
E   RecursionError: maximum recursion depth exceeded in comparison
!!! Recursion detected (same locals & position)
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - RecursionError: maximum recursion...
============================== 1 failed in 0.06s ===============================
