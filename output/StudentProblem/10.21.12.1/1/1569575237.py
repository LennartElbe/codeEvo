============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
___________________________________ test_11 ____________________________________

    def test_11():
>       assert nwords("Hallo was geht") == ["Hallo ", "was ", "geht"]
E       AssertionError: assert ['Hallo was g...'Hallo ', ...] == ['Hallo ', 'was ', 'geht']
E         At index 0 diff: 'Hallo was geht' != 'Hallo '
E         Left contains 11 more items, first extra item: 'Hallo was geht'
E         Use -v to get the full diff

/private/tmp/blabla.py:21: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_11 - AssertionError: assert ['Hallo was g......
============================== 1 failed in 0.05s ===============================
