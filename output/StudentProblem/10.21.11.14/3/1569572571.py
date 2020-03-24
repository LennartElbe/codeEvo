============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp .F                                                    [100%]

=================================== FAILURES ===================================
__________________________________ test_isnt ___________________________________

    def test_isnt():
>       assert leap(2000) == False
E       assert None == False
E        +  where None = leap(2000)

/private/tmp/blabla.py:33: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_isnt - assert None == False
========================= 1 failed, 1 passed in 0.06s ==========================
