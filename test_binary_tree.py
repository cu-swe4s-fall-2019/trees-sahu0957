import unittest
import binary_tree
import random
import os
from os import path

class TestBinaryTree(unittest.TestCase):

    def test_binary_tree_first_entry(self):
        r = binary_tree.insert(root = None, key="key", value=1)
        self.assertEqual((r.key,r.value), ("key", 1))

    def test_binary_tree_insert_left(self):
        root = None
        root = binary_tree.insert(root, key = 10)
        root = binary_tree.insert(root, key = 9)
        self.assertEqual(root.left.key, 9)

    def test_binary_tree_insert_right(self):
        root = None
        root = binary_tree.insert(root, key = 10)
        root = binary_tree.insert(root, key = 11)
        self.assertEqual(root.right.key, 11)

    def test_binary_tree_multiple_right(self):
        root = None
        root = binary_tree.insert(root, key = 10)
        root = binary_tree.insert(root, key = 12)
        root = binary_tree.insert(root, key = 11)
        root = binary_tree.insert(root, key = 13)
        self.assertEqual(root.right.right.key, 13)
        self.assertEqual(root.right.left.key, 11)

    def test_binary_tree_search_None(self):
        root = None
        search = binary_tree.search(root, 1)
        self.assertEqual(root, search)

    def test_binary_tree_search_first(self):
        root = None
        root = binary_tree.insert(root, key = 1, value = 10)
        search = binary_tree.search(root, 1)
        self.assertEqual((root.key, root.value), (1, search))

    def test_binary_tree_search_leftnode(self):
        root = None
        root = binary_tree.insert(root, key = 10, value = 10)
        root = binary_tree.insert(root, key = 9, value = 9)
        search = binary_tree.search(root, 9)
        self.assertEqual((root.left.key, root.left.value), (9, search))

    def test_binary_tree_search_rightnode(self):
        root = None
        root = binary_tree.insert(root, key = 10, value = 10)
        root = binary_tree.insert(root, key = 11, value = 11)
        search = binary_tree.search(root, 11)
        self.assertEqual((root.right.key, root.right.value), (11, search))

    def test_binary_tree_search_noright_or_left_node(self):
        root = None
        root = binary_tree.insert(root, key = 10, value = 10)
        search = binary_tree.search(root, 11)
        self.assertEqual(search, None)
        search = binary_tree.search(root, 9)
        self.assertEqual(search, None)

if __name__ == '__main__':
    unittest.main()
