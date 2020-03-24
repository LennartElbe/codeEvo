============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_divisor _________________________________

    def test_divisor():
>       assert divisior(6) == ["1","2","3","6"]

/private/tmp/blabla.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 6

    def divisior(n: int) -> list:
        """Eine Funktion, die alle Dividenten einer positiven,
        ganzen Zahl in einer Liste wiedergibt
        """
        j = [n]
        for d in range(n+1): #loop bis n
            d > 0
>           if abs(n) % int(d) == 0:
E           ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:15: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisor - ZeroDivisionError: integer divisio...
============================== 1 failed in 0.05s ===============================
