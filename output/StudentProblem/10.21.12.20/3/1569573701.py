============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
        assert leap(1580) == "Ungltige Eingabe"
        assert leap(1900) == False
        assert leap(1600) == True
        assert leap(1601) == False
>       assert leap(-1601) == False
E       AssertionError: assert 'Ungltige Eingabe' == False
E        +  where 'Ungltige Eingabe' = leap(-1601)

/private/tmp/blabla.py:26: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - AssertionError: assert 'Ungltige Eing...
============================== 1 failed in 0.06s ===============================
