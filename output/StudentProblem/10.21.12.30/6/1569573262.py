============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_xs_filt _________________________________

    def test_xs_filt():
        xs1 = [1, 0, 2, 3, -1, -5]
        xs2 = [1, 5, 2, 3, 99, 2.5, 3.5]
>       assert xs_filt(0, xs1) == [0, -1, -5]
E       NameError: name 'xs_filt' is not defined

/private/tmp/blabla.py:31: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_xs_filt - NameError: name 'xs_filt' is not d...
============================== 1 failed in 0.05s ===============================
