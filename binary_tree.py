class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

def insert(root, key, value=None):
    if root == None:
        root = Node(key, value=value)
        return root
    else:
        if key < root.key:
            if root.left == None:
                root.left = Node(key, value = value)
            else:
                insert(root.left, key, value = value)
        else:
            if root.right == None:
                root.right = Node(key, value = value)
            else:
                insert(root.right, key, value = value)
        return root

def search(root, key):
    return None
