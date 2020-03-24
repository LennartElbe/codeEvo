============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test_5 ____________________________________

    def test_5():
>       assert divisors(10) == [1, 2, 5, 10]

/private/tmp/blabla.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 10

    def divisors(x: int):
        result = []
        for i in range(1, x + 1):
            if not(x % i):
>               reasult.append(i)
E               NameError: name 'reasult' is not defined

/private/tmp/blabla.py:12: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_5 - NameError: name 'reasult' is not defined
============================== 1 failed in 0.04s ===============================
