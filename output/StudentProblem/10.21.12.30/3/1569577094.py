============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
        assert leap(1600) == True, "Fall: durch 4, 100 und 400 teilbar"
        assert leap(1604) == True, "Fall: nur durch 4 teilbar"
        assert leap(1603) == False, "Fall: nicht durch 4 teilbar"
>       assert leap(1700) == False, "Fall: durch 4 und 100 teilbar, nicht durch 400 teilbar"
E       AssertionError: Fall: durch 4 und 100 teilbar, nicht durch 400 teilbar
E       assert True == False
E        +  where True = leap(1700)

/private/tmp/blabla.py:41: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: Fall: durch 4 und 100...
============================== 1 failed in 0.05s ===============================
