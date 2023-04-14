'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


<<<<<<< HEAD
class AVLTree(BST):
=======
class AVLTree():
>>>>>>> heap
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
<<<<<<< HEAD
        super().__init__(xs)
=======
>>>>>>> heap

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
<<<<<<< HEAD
        if node is None:
            return True
        bf = AVLTree._balance_factor(node)
        if abs(bf) > 1:
            return False
        return AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)
=======
>>>>>>> heap

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
<<<<<<< HEAD
        if node is None or node.right is None:
            return node
        new_node = Node(node.right.value)
        new_node.right = node.right.right
        new_left = Node(node.value)
        new_left.left = node.left
        new_left.right = node.right.left
        new_node.left = new_left
        return new_node
=======
>>>>>>> heap

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
<<<<<<< HEAD
        if node is None or node.left is None:
            return node
        new_node = Node(node.left.value)
        new_node.left = node.left.left
        new_right = Node(node.value)
        new_right.right = node.right
        new_right.left = node.left.right
        new_node.right = new_right
        return new_node
=======
>>>>>>> heap

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
<<<<<<< HEAD
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        balance = AVLTree._balance_factor(node)
        if balance > 1:
            if value < node.left.value:
                node = AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
        elif balance < -1:
            if value > node.right.value:
                node = AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
        return node
=======
>>>>>>> heap

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
<<<<<<< HEAD
        balance = AVLTree._balance_factor(node)
        right = AVLTree._balance_factor(node.right)
        left = AVLTree._balance_factor(node.left)
        if balance < -1:
            if right > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        elif balance > 1:
            if left < 0:
                node.left = AVLTree._left_rotate(node)
            return AVLTree._right_rotate(node)
        else:
            return node
=======
>>>>>>> heap
