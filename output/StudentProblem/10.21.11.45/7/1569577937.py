============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert divisors(4,2) == [2,1]

/private/tmp/blabla.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 4, d = 2

    def divisors(n, d):
        result = []
        if n <= 0:
            return result
        else:
            for i in range(1,n):
                if i % d != 0:
                    continue
                else:
                    result.append(i)
>                   return rresult
E                   NameError: name 'rresult' is not defined

/private/tmp/blabla.py:18: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - NameError: name 'rresult' is not defined
============================== 1 failed in 0.05s ===============================
