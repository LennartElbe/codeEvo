============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(1) == [1]

/private/tmp/blabla.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 1

    def divisors(n)->list:
        teiler = []
        if n < 0:
            return "Ungltige Eingabe"
        else:
            for i in range(1, n+1):
                if n%i == 0:
>                   teiler += i
E                   TypeError: 'int' object is not iterable

/private/tmp/blabla.py:15: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - TypeError: 'int' object is not it...
============================== 1 failed in 0.06s ===============================
