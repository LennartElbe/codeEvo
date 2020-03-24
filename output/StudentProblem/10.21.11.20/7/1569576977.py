============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisior _________________________________

    def test_divisior():
>       assert divisior(6) == ["1","2","3","6"]
E       AssertionError: assert [6, '1'] == ['1', '2', '3', '6']
E         At index 0 diff: 6 != '1'
E         Right contains 2 more items, first extra item: '3'
E         Use -v to get the full diff

/private/tmp/blabla.py:23: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisior - AssertionError: assert [6, '1'] =...
============================== 1 failed in 0.04s ===============================
