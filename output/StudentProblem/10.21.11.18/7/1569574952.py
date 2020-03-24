============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(10)

/private/tmp/blabla.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 10

    def divisors(n: int) -> list:
>       if d // n == 0:
E       NameError: name 'd' is not defined

/private/tmp/blabla.py:9: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - NameError: name 'd' is not defined
============================== 1 failed in 0.05s ===============================
