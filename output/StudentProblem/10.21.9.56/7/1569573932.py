============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(2) == [2,4,6,8]

/private/tmp/blabla.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/private/tmp/blabla.py:10: in divisors
    d = int(input())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x103d09f10>, args = ()

    def read(self, *args):
        raise IOError(
>           "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

../../../Library/Python/3.7/lib/python/site-packages/_pytest/capture.py:725: OSError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - OSError: pytest: reading from std...
============================== 1 failed in 0.07s ===============================
