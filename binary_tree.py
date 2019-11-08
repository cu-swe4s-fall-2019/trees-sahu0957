class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value=None):
    if root is None:
        # If the root doesn't exist, then create the node
        root = Node(key, value=value)
        return root
    else:
        # if the root exists, it's time to check whether our key goes right
        # or left of the existing root
        if key < root.key:
            # if the new key is less than our root key, it goes to the left
            if root.left is None:
                root.left = Node(key, value=value)
            else:
                # if the left is already occupied, it means we
                # need to determine whether it goes left or
                # right of this node, triggering a recursion
                insert(root.left, key, value=value)
        else:
            # if it's greater than our root key, it goes to the right
            if root.right is None:
                root.right = Node(key, value=value)
            else:
                # if the right is already occupied,
                # we need to determine whether it
                # goes right or
                # left of this node, triggering a recursion
                insert(root.right, key, value=value)
        return root


def search(root, key):
    if root is None:
        # If our root is none, that means this node is empty, and thus there's
        # no value here
        return None
    elif root.key == key:
        # If our key matches, great! Return the associated value and exit
        # the recursive loop
        return root.value
    elif key < root.key and root.left is not None:
        # If the key is less than our root key, search the left node, which
        # triggers a recursion
        return search(root.left, key)
    elif key > root.key and root.right is not None:
        # If the key is greater than our root key, search the right node, which
        # triggers a recursion
        return search(root.right, key)

    return None
