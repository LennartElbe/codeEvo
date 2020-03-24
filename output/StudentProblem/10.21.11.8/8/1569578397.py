============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp FF                                                    [100%]

=================================== FAILURES ===================================
________________________________ test_postorder ________________________________

    def test_postorder():
>       assert Node (Leaf(1), Leaf(2), 3).postorder() == [1, 2, 3]

/private/tmp/blabla.py:103: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <blabla.Node object at 0x1111d7b90>

    def postorder(self):
        """A function that implements the post order method of a
        given node object.
    
        It returns the ordered tree in post order notation.
        If the value of a given node is None, than it won't be added
        to the output, but it's leaves will.
    
        Args:
            a node object
        Returns:
            a list of the post order notation of the node.
        """
        if self.value is None:
            return [postorder(self.left),
                    postorder(self.right)]
        else:
>           return [postorder(self.left),
                    postorder(self.right),
                    postorder(self.value)]
E           NameError: name 'postorder' is not defined

/private/tmp/blabla.py:97: NameError
________________________________ test_preorder _________________________________

    def test_preorder():
>       assert Node (Leaf(1), Leaf(2), 3).postorder() == [3, 1, 2]

/private/tmp/blabla.py:111: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <blabla.Node object at 0x1111d6490>

    def postorder(self):
        """A function that implements the post order method of a
        given node object.
    
        It returns the ordered tree in post order notation.
        If the value of a given node is None, than it won't be added
        to the output, but it's leaves will.
    
        Args:
            a node object
        Returns:
            a list of the post order notation of the node.
        """
        if self.value is None:
            return [postorder(self.left),
                    postorder(self.right)]
        else:
>           return [postorder(self.left),
                    postorder(self.right),
                    postorder(self.value)]
E           NameError: name 'postorder' is not defined

/private/tmp/blabla.py:97: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_postorder - NameError: name 'postorder' is n...
FAILED ../../../../../tmp/::test_preorder - NameError: name 'postorder' is no...
============================== 2 failed in 0.08s ===============================
