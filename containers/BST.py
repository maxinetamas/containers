'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree file.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    That means that the BST class "inherits" all of the methods from BinaryTree,
    and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
<<<<<<< HEAD
        if xs is not None:
            for x in xs:
                self.insert(x)

    def __iter__(self):
        return self._inorder_iter(self.root)

    def _inorder_iter(self, node):
        if node is not None:
            yield from self._inorder_iter(node.left)
            yield node.value
            yield from self._inorder_iter(node.right)
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

<<<<<<< HEAD
=======
    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.

        NOTE:
        We only care about "semantic" equality,
        and not "syntactic" equality.
        That is, we do not care about the tree structure itself,
        and only care about the contents of what the tree contains.

        HINT:
        Convert the contents of both trees into a sorted list,
        then compare those sorted lists for equality.
        '''

>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993
    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:
        it only checks if the children of the current node are less than/greater than,
        rather than ensuring that all nodes to the left/right are less than/greater than.

        HINT:
        Use the _find_smallest and _find_largest functions to fix the bug.
        You should use the _ prefixed methods because those are static methods just like this one.
        '''
        ret = True
<<<<<<< HEAD
        if node is None:
            return ret
        if node.left:
            if node.value > BST._find_largest(node.left).value:
=======
        if node.left:
            if node.value >= node.left.value:
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
<<<<<<< HEAD
            if node.value < BST._find_smallest(node.right).value:
=======
            if node.value <= node.right.value:
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.

        FIXME:
        Implement this function.

        HINT:
        Create a staticmethod helper function following the pattern of _is_bst_satisfied.
        '''
<<<<<<< HEAD
        self.root = BST._insert_helper(self.root, value)

    @staticmethod
    def _insert_helper(node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = BST._insert_helper(node.left, value)
        elif value > node.value:
            node.right = BST._insert_helper(node.right, value)
        return node
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.

        HINT:
        Repeatedly call the insert method.
        You cannot get this method to work correctly until you have gotten insert to work correctly.
        '''
<<<<<<< HEAD
        for x in xs:
            self.insert(x)
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
<<<<<<< HEAD
        return self._find(value, self.root)
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
<<<<<<< HEAD
        if node is None:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return BST._find(value, node.left)
        else:
            return BST._find(value, node.right)
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
<<<<<<< HEAD
            return BST._find_smallest(self.root).value
=======
            return BST._find_smallest(self.root)
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    @staticmethod
    def _find_smallest(node):
        '''
        This is a helper function for find_smallest and not intended to be called directly by the user.
        '''
<<<<<<< HEAD
        if node.left is None:
            return node
=======
        assert node is not None
        if node.left is None:
            return node.value
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Follow the pattern of the _find_smallest function.
        '''
<<<<<<< HEAD
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root).value

    @staticmethod
    def _find_largest(node):
        if node.right is None:
            return node
        else:
            return BST._find_largest(node.right)
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        You should have everything else working before you implement this function.

        HINT:
        Use a recursive helper function.
        '''
<<<<<<< HEAD
        self.root = BST._remove_helper(self.root, value)

    @staticmethod
    def _remove_helper(node, value):
        if node is None:
            return None
        if value > node.value:
            node.right = BST._remove_helper(node.right, value)
        elif value < node.value:
            node.left = BST._remove_helper(node.left, value)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                newnode = node.right
                while newnode.left is not None:
                    newnode = newnode.left
                node.value = newnode.value
                node.right = BST._remove_helper(node.right, newnode.value)
        return node
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.

        HINT:
        See the insert_list function.
        '''
<<<<<<< HEAD
        for x in xs:
            self.remove(x)
=======
>>>>>>> 66def44ebc60cc47992071c3f591a151895e1993
