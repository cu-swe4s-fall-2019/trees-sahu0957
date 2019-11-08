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

if __name__ == '__main__':
    unittest.main()
