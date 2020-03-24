============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test_4 ____________________________________

    def test_4():
>       assert leap(2000) == True

/private/tmp/blabla.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 2000

    def leap(x):
>       if x / 4 and X /100 and X / 400:
E       NameError: name 'X' is not defined

/private/tmp/blabla.py:8: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_4 - NameError: name 'X' is not defined
============================== 1 failed in 0.05s ===============================
