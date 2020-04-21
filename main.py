""" Module for using tree """
from modules.avl_tree import AVLTree

tree = AVLTree()
tree.insert(20)
print(tree.search(20))
print(tree.search(30))
print(tree.search(20, True))
tree.insert(20)
tree.insert(40)
tree.insert(50)