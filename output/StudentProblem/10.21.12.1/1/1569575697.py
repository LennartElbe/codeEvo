============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
___________________________________ test_11 ____________________________________

    def test_11():
>       assert nwords("Hallo ") == ["Hallo "]
E       AssertionError: assert ['Hallo ', 'H...o ', 'Hallo '] == ['Hallo ']
E         Left contains 5 more items, first extra item: 'Hallo '
E         Use -v to get the full diff

/private/tmp/blabla.py:21: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_11 - AssertionError: assert ['Hallo ', 'H......
============================== 1 failed in 0.05s ===============================
