'''
AVL tree is a form of balanced BST. 
https://youtu.be/q4fnJZr8ztY
'''
from BST import BST

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
    
    def height(self, node):
        return node.height

    def balance_factor(self, node):
        return node.bf

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
                if node.bf < 0:
                    # Take the rightmost element of left sub-tree and replace it with current_node
                    new_node = self.find_max(node.left)
                    node.data = new_node.data
                    # Remove the replaced node to avoid repetition
                    node.left = self._remove_r(new_node.data, node.left)
                else:
                    new_node = self.find_min(node.right)         
                    node.data = new_node.data
                    node.right = self._remove_r(new_node.data, node.right)
        
        # Only change from bst to avl tree - update heights and balance node
        self.update(node)
        return self.balance(node)
    
    # Update the height and balancing factor of node
    def update(self, node):
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        node.height = 1 + max(left_height, right_height)

        # BF taken right height - left height
        node.bf = right_height - left_height

    def balance(self, node):
        # left weighted
        if node.bf == -2:
            # left-left case
            if node.left.bf <=0:
                node = self.left_left_case(node)
            # left-right case
            else:
                node = self.left_right_case(node)
        
        # Right weighted
        if node.bf == 2:
            # right-right case
            if node.right.bf >=0:
                node = self.right_right_case(node)
            # right-left case
            else:
                node = self.right_left_case(node)
        # bf of 0,1,-1 is fine
        return node
    
    # Rotation cases function
    def left_left_case(self, node):
        return self.right_rotate(node)
    
    def left_right_case(self, node):
        node.left = self.left_rotate(node.left)
        return self.left_left_case(node)

    def right_right_case(self, node):
        return self.left_rotate(node)

    def right_left_case(self, node):
        node.right = self.right_rotate(node.right)
        return self.right_right_case(node)

    # Individual rotations
    def left_rotate(self, node):
        parent = node.right
        node.right = parent.left
        parent.left = node
        # update heights
        self.update(node)
        self.update(parent)
        return parent

    def right_rotate(self, node):
        parent = node.left
        node.left = parent.right
        parent.right = node

        self.update(node)
        self.update(parent)
        return parent
    
    # All other utility functions like contains(), size(), findmax() are inherited from BST

if __name__ == "__main__":
    # Testing AVL tree
    #                   10
    #           7                 16
    #       3         9        14
    #   1     5     8       12    15
    #          6              13
    avl = AVLTree([10,7,3,1,5,6,9,8,16,14,12,13,15])
    avl.inorder_traversal()
    print()
    avl.level_order()
    avl.preorder_traversal()
    print()
    avl.remove(7)
    avl.remove(6)
    avl.remove(8)
    avl.level_order()