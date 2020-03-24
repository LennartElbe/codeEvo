============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(10, 5)
E       assert None
E        +  where None = divisors(10, 5)

/private/tmp/blabla.py:19: AssertionError
----------------------------- Captured stdout call -----------------------------
Teiler
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert None
============================== 1 failed in 0.05s ===============================
