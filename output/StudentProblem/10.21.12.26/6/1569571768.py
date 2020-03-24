============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       list_filter(5, [1,1,3,5,9]) == [1,1,3,5]

/private/tmp/blabla.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 5, xs = [1, 1, 3, 5, 9]

    def list_filter(x:int ,xs:list) -> list:
        result = []
        for i in xs:
            if x > i:
>               append.result(i)
E               NameError: name 'append' is not defined

/private/tmp/blabla.py:12: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - NameError: name 'append' is not defined
============================== 1 failed in 0.06s ===============================
