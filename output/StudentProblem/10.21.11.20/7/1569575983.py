============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisior _________________________________

    def test_divisior():
>       assert divisior(6) == ["1","2","3","6"]

/private/tmp/blabla.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 6

    def divisior(n: int) -> list:
        """Eine Funktion, die alle Dividenten einer positiven,
        ganzen Zahl in einer Liste wiedergibt
        """
        j = [n]
>       d > 0
E       UnboundLocalError: local variable 'd' referenced before assignment

/private/tmp/blabla.py:13: UnboundLocalError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisior - UnboundLocalError: local variable...
============================== 1 failed in 0.04s ===============================
