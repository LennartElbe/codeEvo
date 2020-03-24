============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(4) == [1, 2, 4]

/private/tmp/blabla.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 4

    def divisors(x: int) -> list:
        divisors_list = []
        i = 1
        if x == 0:
            return []
        while i <= x:
            if x%i == 0:
>               divisors.append(x)
E               AttributeError: 'function' object has no attribute 'append'

/private/tmp/blabla.py:15: AttributeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - AttributeError: 'function' object...
============================== 1 failed in 0.06s ===============================
