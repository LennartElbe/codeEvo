============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp FF                                                    [100%]

=================================== FAILURES ===================================
___________________________________ test_11 ____________________________________

    def test_11():
>       assert nwords("Hallo ") == ["Hallo "]
E       AssertionError: assert ['Hallo ', 'H...o ', 'Hallo '] == ['Hallo ']
E         Left contains 5 more items, first extra item: 'Hallo '
E         Use -v to get the full diff

/private/tmp/blabla.py:21: AssertionError
_____________________________________ test _____________________________________

    def test():
>       assert word_count("/usr/share/doc/libpython3.6-minimal/copyright") == (995,7030, 49852)

/private/tmp/blabla.py:49: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

f = '/usr/share/doc/libpython3.6-minimal/copyright'

    def word_count(f):
        line_num = 0
        word_num = 0
        ze_num = 0
>       with open(r, f) as e:
E       NameError: name 'r' is not defined

/private/tmp/blabla.py:38: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_11 - AssertionError: assert ['Hallo ', 'H......
FAILED ../../../../../tmp/::test - NameError: name 'r' is not defined
============================== 2 failed in 0.05s ===============================
