''' 
A basic implementation for a binary tree. Can be inherited for further binary tree implementations.
''' 
class BinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            # Initializing Binary tree node with data, left and right child
            self.data = data
            self.left = left
            self.right = right
        
    def __init__(self):
        self.root = None
        self.node_count = 0