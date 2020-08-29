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

