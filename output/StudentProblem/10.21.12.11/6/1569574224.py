============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp .F                                                    [100%]

=================================== FAILURES ===================================
__________________________________ test_list ___________________________________

    def test_list():
>       assert [5] == [6]
E       assert [5] == [6]
E         At index 0 diff: 5 != 6
E         Use -v to get the full diff

/private/tmp/blabla.py:23: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list - assert [5] == [6]
========================= 1 failed, 1 passed in 0.06s ==========================
