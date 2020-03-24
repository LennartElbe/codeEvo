============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert leap(1900) == True

/private/tmp/blabla.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 1900

    def leap(x: int):
        """Checks if a given year is a leap year(after 1582).
        Args:
            x: int(a year)
    
        Returns:
            True or False(or an exception).
        """
        if x < 1582:
            return("The gregorian calendar wasn'n invented yet")
        else:
            if x%100 == 0 and x%400 != 0:
>               return false
E               NameError: name 'false' is not defined

/private/tmp/blabla.py:19: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - NameError: name 'false' is not defined
============================== 1 failed in 0.05s ===============================
