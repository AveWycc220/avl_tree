""" Module for using tree """
from modules.avl_tree import AVLTree

tree = AVLTree()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(18)
tree.insert(25)
tree.delete(20)
print(tree.search(10, True))
print(tree.search(5, True))
print(tree.search(20, True))
print(tree.search(18, True))
print(tree.search(25, True))
