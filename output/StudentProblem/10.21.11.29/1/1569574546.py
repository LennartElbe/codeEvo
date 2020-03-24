============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
>       assert (nwords("Ha Ho") == ["H", "a", "H", "o"])
E       AssertionError: assert ['H', 'a', ' ', 'H', 'o'] == ['H', 'a', 'H', 'o']
E         At index 2 diff: ' ' != 'H'
E         Left contains one more item: 'o'
E         Use -v to get the full diff

/private/tmp/blabla.py:14: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - AssertionError: assert ['H', 'a', '...
============================== 1 failed in 0.05s ===============================
