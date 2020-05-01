""" Module for test class - Set """
from modules.set.set import Set
import unittest

class TestSetAPI(unittest.TestCase):
    """ Class for test methods of set """
    # pylint: disable=W0212
    # W0212 - Access to a protected member
    def setUp(self):
        """ Start """

    def test_init(self):
        """ Test __init__ """
        # Default
        new_set = Set('int')
        self.assertEqual(str(type(new_set._Set__tree)), "<class 'modules.tree.avl_tree.AVLTree'>")
        self.assertEqual(new_set._Set__set_type, 'int')
        # Wrong type
        w_set = Set('ga')
        self.assertEqual(w_set._Set__set_type, None)

    def test_add(self):
        """ Test add() """
        # Default
        default_set = Set('int')
        default_set.add('5')
        default_set.add('8')
        default_set.add('10')
        self.assertEqual(default_set.contains('5'), True)
        self.assertEqual(default_set.contains('8'), True)
        self.assertEqual(default_set.contains('10'), True)
        # Wrong input
        wront_set = Set('int')
        wront_set.add('dasg')
        self.assertEqual(wront_set.count(), 0)
        # int : immutable
        int_set = Set('int')
        int_set.add('15')
        self.assertEqual(int_set.contains('15'), True)
        # list : mutable
        list_set = Set('list')
        list_set.add('[16, 167]')
        self.assertEqual(list_set.contains('[16, 167]'), True)
        # Add after delete
        del_set = Set('int')
        del_set.add('15')
        del_set.remove('15')
        del_set.add('15')
        self.assertEqual(del_set.contains('15'), True)
        # Same add
        same_set = Set('int')
        same_set.add('5')
        same_set.add('5')
        self.assertEqual(same_set.count(), 1)

    def test_remove(self):
        """ Test remove() """
        # Default
        default_set = Set('int')
        default_set.add('5')
        default_set.add('8')
        default_set.remove('5')
        self.assertEqual(default_set.contains('5'), False)
        default_set.add('6')
        self.assertEqual(default_set.contains('6'), True)
        default_set.remove('6')
        self.assertEqual(default_set.contains('6'), False)
        # Wrong input
        wrong_set = Set('int')
        wrong_set.add('5')
        wrong_set.remove('gsdg')
        self.assertEqual(wrong_set.count(), 1)
        # int : immutable
        int_set = Set('int')
        int_set.add('15')
        int_set.remove('15')
        self.assertEqual(int_set.contains('15'), False)
        # list : mutable
        list_set = Set('list')
        list_set.add('[16, 167]')
        list_set.remove('[16, 167]')
        self.assertEqual(list_set.contains('[16, 167]'), False)
        # Empty
        empty_set = Set('int')
        empty_set.remove('5')
        self.assertEqual(empty_set.count(), 0)
        self.assertEqual(empty_set.is_empty(), True)

    def test_contains(self):
        """ Test contains() """
        # Default
        default_set = Set('int')
        default_set.add('5')
        default_set.add('8')
        default_set.add('10')
        self.assertEqual(default_set.contains('5'), True)
        self.assertEqual(default_set.contains('8'), True)
        self.assertEqual(default_set.contains('10'), True)
        # Empty
        empty_set = Set('int')
        self.assertEqual(empty_set.contains('5'), False)
        # int : immutable
        int_set = Set('int')
        int_set.add('15')
        self.assertEqual(int_set.contains('15'), True)
        # list : mutable
        list_set = Set('list')
        list_set.add('[16, 167]')
        self.assertEqual(list_set.contains('[16, 167]'), True)
        # After remove
        del_set = Set('int')
        del_set.add('5')
        del_set.remove('5')
        self.assertEqual(del_set.contains('5'), False)
        # Wrong input
        wron_set = Set('int')
        wron_set.add('5')
        self.assertEqual(del_set.contains('ag'), "TypeError : Wrong Input")

    def test_clear(self):
        """ Test clear() """
        new_set = Set('int')
        self.assertEqual(new_set.is_empty(), True)
        new_set.add('5')
        self.assertEqual(new_set.is_empty(), False)

    def test_count(self):
        """ Test count() """
        new_set = Set('int')
        self.assertEqual(new_set.count(), 0)
        new_set.add('5')
        self.assertEqual(new_set.count(), 1)
        new_set.add('567')
        self.assertEqual(new_set.count(), 2)
        for i in range(0, 10):
            new_set.add(F'{i}')
        self.assertEqual(new_set.count(), 11)
        new_set.remove('5')
        self.assertEqual(new_set.count(), 10)
        new_set.clear()
        self.assertEqual(new_set.count(), 0)

    def test_is_empty(self):
        """ Test is_empty() """
        new_set = Set('int')
        self.assertEqual(new_set.is_empty(), True)
        new_set.add('5')
        self.assertEqual(new_set.is_empty(), False)
        new_set.clear()
        self.assertEqual(new_set.is_empty(), True)
        new_set.add('6')
        self.assertEqual(new_set.is_empty(), False)
        new_set.remove('6')
        self.assertEqual(new_set.is_empty(), True)