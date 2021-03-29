'''
AVL tree is a form of balanced BST. 
https://youtu.be/q4fnJZr8ztY
'''
from .BST import BST

# AVL tree class inherits BST class from BST.py
class AVLTree(BST):
    # Node of AVL tree (overrides BST node)
    class Node:
        def __init__(self, data, left=None, right=None):
            self.bf = 0     # Balancing factor
            self.height = 0 # Height of the node in tree

            self.data = data
            self.left = left
            self.right = right
    
    def __init__(self, value_list):
        super().__init__(value_list)
    
    # Overriding the BST's insert method
    def _insert_r(self, data, node):
        # Base case: found leaf node
        if node is None:
            return self.Node(data)
        if data < node.data:
            node.left = self._insert_r(data, node.left)
        else:
            node.right = self._insert_r(data, node.right)
        # Only change from bst to avl tree - update heights and balance node
        self.update(node)
        return self.balance(node)

    # Overriding the BST's remove method
    def _remove_r(self, data, node):
        if node is None:    return None

        # Dig into(traverse) the tree to find the node we are looking for:
        if data < node.data:
            node.left = self._remove_r(data, node.left)
        elif data > node.data:
            node.right = self._remove_r(data, node.right)
        # if the node to be deleted is `node`
        else:

            # if left tree is null:
            if node.left is None:
                # Make current node as right tree                
                return node.left

            # If right tree is null
            elif node.right is None:
                # Make current node as left tree
                return node.right

            # If both sub-tree is present
            else:
                # Take the rightmost element of left sub-tree and replace it with current_node
                new_node = self.find_max(node.left)         # function from BST
                node.data = new_node.data
                # Remove the replaced node to avoid repetition
                node.left = self._remove_r(new_node.data, node.left)
        
        # Only change from bst to avl tree - update heights and balance node
        self.update(node)
        return self.balance(node)

    