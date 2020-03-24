============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
___________________________________ test_wci ___________________________________

    def test_wci():
>       assert(word_count_iter(["dg   ja n", "dg   ja n  "] == (2, 6, 20))

/private/tmp/blabla.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

it = False

    def word_count_iter(it):
        nz = 0
        nw = 0
        nc = 0
>       for z in it:
E       TypeError: 'bool' object is not iterable

/private/tmp/blabla.py:32: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_wci - TypeError: 'bool' object is not iterable
============================== 1 failed in 0.06s ===============================
