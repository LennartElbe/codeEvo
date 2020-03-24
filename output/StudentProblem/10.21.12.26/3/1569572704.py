============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert leap (1500) == false

/private/tmp/blabla.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 1500

    def leap (x:int)->bool:
        if x < 1582:
>           return false
E           NameError: name 'false' is not defined

/private/tmp/blabla.py:9: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - NameError: name 'false' is not defined
============================== 1 failed in 0.06s ===============================
