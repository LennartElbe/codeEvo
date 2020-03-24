============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert Node(Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]

/private/tmp/blabla.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

Node = <blabla.Node object at 0x1023b0850>

    def postorder(Node):
        if Node is None:
            pass
        else:
>           return[postorder(Node.left), postorder(Node.right), Node.value]
E           NameError: name 'postorder' is not defined

/private/tmp/blabla.py:31: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - NameError: name 'postorder' is not defined
============================== 1 failed in 0.05s ===============================
