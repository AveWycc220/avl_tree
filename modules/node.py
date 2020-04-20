""" Module for elements in tree """

class Node():
    """ Class for elements in tree """
    def __init__(self, value=None):
        """ Initialization """
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        self.height = 0
    def __str__(self):
        """ Output information """
        return F"Node({self.value}, Height: {self.height}"
        