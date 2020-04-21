""" Module for elements in tree """
from modules.node import Node

class AVLTree():
    """ Class of avl_tree. """
    def __init__(self):
        """ Initialization """
        self.root = None
        self.node_count = 0
    def set_root(self, val):
        """ Set the root value """
        self.root = Node(val)
    def insert(self, val):
        """ Insert a val into AVLTree """
        if self.root is None:
            self.set_root(val)
        else:
            self._insert_node(self.root, val)
        self.node_count += 1
    def _insert_node(self, current_node, val):
        """ Help 'def insert()' to insert a value into tree. """
        node_to_rebalance = None
        if current_node.value > val:
            if current_node.left:
                self._insert_node(current_node.left, val)
            else:
                new_node = Node(val)
                current_node.left = new_node
                new_node.parent = current_node
                if current_node.height == 0:
                    self._recompute_heights(current_node)
                    node = current_node
                    while node:
                        if node.balance_factor() in [-2, 2]:
                            node_to_rebalance = node
                            break
                        node = node.parent
        else:
            if current_node.right:
                self._insert_node(current_node.right, val)
            else:
                new_node = Node(val)
                current_node.right = new_node
                new_node.parent = current_node
                if current_node.height == 0:
                    self._recompute_heights(current_node)
                    node = current_node
                    while node:
                        if node.balance_factor() in [-2, 2]:
                            node_to_rebalance = node
                            break
                        node = node.parent
        if node_to_rebalance:
            self._rebalance(node_to_rebalance)
    @staticmethod
    def _recompute_heights(start_node):
        """ Change height of elements after operation """
        changed = True
        node = start_node
        while node and changed:
            old_height = node.height
            node.height = (node.max_children_height() + 1 if (node.right or node.left) else 0)
            changed = node.height != old_height
            node = node.parent
    def _rebalance(self, node_to_rebalance):
        """ Method for balance tree """
        if node_to_rebalance.balance_factor() == -2:
            if node_to_rebalance.right.balance_factor() <= 0:
                self._rrc(node_to_rebalance)
            else:
                self._rlc(node_to_rebalance)
        if node_to_rebalance.balance_factor() == +2:
            if node_to_rebalance.left.balance_factor() >= 0:
                self._llc(node_to_rebalance)
            else:
                self._lrc(node_to_rebalance)
    def _rrc(self, A):
        """ Right-right-case (single left rotation). """
        F = A.parent
        B = A.right
        C = B.right
        assert (not A is None and not B is None and not C is None)
        A.right = B.left
        if A.right:
            A.right.parent = A
        B.left = A
        A.parent = B
        if F is None:
            self.root = B
            self.root.parent = None
        else:
            if F.right == A:
                F.right = B
            else:
                F.left = B
            B.parent = F
        self._recompute_heights(A)
        self._recompute_heights(B.parent)
    def _rlc(self, A):
        """ Right-left-case (double left rotation). """
        F = A.parent
        B = A.right
        C = B.left
        assert (not A is None and not B is None and not C is None)
        B.left = C.right
        if B.left:
            B.left.parent = B
        A.right = C.left
        if A.right:
            A.right.parent = A
        C.right = B
        B.parent = C
        C.left = A
        A.parent = C
        if F is None:
            self.root = C
            self.root.parent = None
        else:
            if F.right == A:
                F.right = C
            else:
                F.left = C
            C.parent = F
        self._recompute_heights(A)
        self._recompute_heights(B)
    def _llc(self, A):
        """ Left-left-case (single right rotation). """
        F = A.parent
        B = A.left
        C = B.left
        assert (not A is None and not B is None and not C is None)
        A.left = B.right
        if A.left:
            A.left.parent = A
        B.right = A
        A.parent = B
        if F is None:
            self.root = B
            self.root.parent = None
        else:
            if F.right == A:
                F.right = B
            else:
                F.left = B
                B.parent = F
        self._recompute_heights(A)
        self._recompute_heights(B.parent)
    def _lrc(self, A):
        """ Left-right-case (double right rotation). """
        F = A.parent
        B = A.left
        C = B.right
        assert (not A is None and not B is None and not C is None)
        A.left = C.right
        if A.left:
            A.left.parent = A
        B.right = C.left
        if B.right:
            B.right.parent = B
        C.left = B
        B.parent = C
        C.right = A
        A.parent = C
        if F is None:
            self.root = C
            self.root.parent = None
        else:
            if F.right == A:
                F.right = C
            else:
                F.left = C
                C.parent = F
        self._recompute_heights(A)
        self._recompute_heights(B)
