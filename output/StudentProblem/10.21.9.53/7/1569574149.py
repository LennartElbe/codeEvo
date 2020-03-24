============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_divisors_a ________________________________

    def test_divisors_a():
        zahl = 16
>       assert divisors(zahl) == [1, 2, 4, 8, 16]

/private/tmp/blabla.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 16

    def divisors(n) -> list:
        """
    
        """
        ret_list = []
>       while (i <= n):
E       UnboundLocalError: local variable 'i' referenced before assignment

/private/tmp/blabla.py:13: UnboundLocalError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors_a - UnboundLocalError: local variab...
============================== 1 failed in 0.05s ===============================
