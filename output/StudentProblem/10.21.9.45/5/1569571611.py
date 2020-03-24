============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test_2 ____________________________________

>   def test_2():  assert mysum([1,2,3]) == 6

/private/tmp/blabla.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

zs = [1, 2, 3]

>   def mysum(zs:list) -> int:  return sum(xs)
E   NameError: name 'xs' is not defined

/private/tmp/blabla.py:9: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_2 - NameError: name 'xs' is not defined
============================== 1 failed in 0.07s ===============================
