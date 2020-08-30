class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if root.data <= node.data:
        root.right = insert(root.right, node)
    else:
        root.left = insert(root.left, node)
    return root

def search(root, data):
    if root.data == data:
        return True
    elif root.data < data:
        return search(root.right, data)
    else:
        return search(root.left, data)
