============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisior _________________________________

    def test_divisior():
>       assert divisior(6) == ["1","2","3","6"]

/private/tmp/blabla.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 6

    def divisior(n: int) -> list:
        """Eine Funktion, die alle Dividenten einer positiven,
        ganzen Zahl in einer Liste wiedergibt
        """
        j = [n]
        for d in range(n+1): #loop bis n
>           if int(n) % int(d) == 0:
E           ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:14: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisior - ZeroDivisionError: integer divisi...
============================== 1 failed in 0.04s ===============================
