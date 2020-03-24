============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert leap(155) == 'jahrzahl ist kleiner als 1582'

/private/tmp/blabla.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

jahrzahl = 155

    def leap(jahrzahl: int) -> bool:
        'return True if the given year is schaltjahr and false if not'
>       schaltjahr == True
E       NameError: name 'schaltjahr' is not defined

/private/tmp/blabla.py:9: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - NameError: name 'schaltjahr' is not d...
============================== 1 failed in 0.05s ===============================
