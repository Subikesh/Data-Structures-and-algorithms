''' 
Kruskal's algo for finding minimum spanning tree
Source - https://www.youtube.com/watch?v=KbFlZYCpONw&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=25
'''
class UnionFind:
    # Number of elements
    size = 0

    # Size of components
    c_size = []

    # parent[i] points to the parent of i, if parent[i] = i it is root node
    parent = []

    # Total number of components in union find
    num_components = 0

    def __init__(self, size):
        if size <= 0:
            raise ValueError("value of size must be positive")
        self.size = self.num_components = size
        self.c_size = [1 for _ in range(size)]
        self.parent = [i for i in range(size)]

    # returns the root node of particular element and does path compression
    def find(self, elem):
        root = elem
        # Finding root node
        # Loop till root_node(node which has self loop)
        while root != self.parent[root]:
            root = self.parent[root]

        # Path compression - https://www.youtube.com/watch?v=VHRhJWacxis&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=22
        while elem != root:
            parent = self.parent[elem]
            self.parent[elem] = root
            elem = parent
        return root

    # return if elem1 and 2 are on same component
    def connected(self, elem1, elem2):
        return self.find(elem1) == self.find(elem2)
    
    # Return the size of the components/set 'elem' belongs to
    def component_size(self, elem):
        return self.c_size[self.find(elem)]

    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, elem1, elem2):
        print("Unifying", elem1, 'and', elem2)
        # If both elements are already in same component
        if(self.connected(elem1, elem2)): 
            return None
        
        root1, root2 = self.find(elem1), self.find(elem2)
        
        # Joining component with less elements with component with more elements
        if self.c_size[root1] > self.c_size[root2]:
            self.parent[root2] = root1
            self.c_size[root1] += self.c_size[root2]
        else:
            self.parent[root1] = root2
            self.c_size[root2] += self.c_size[root1]
        
        # Since unified, number of components decremented
        self.num_components -= 1

    # Display current state of elements
    def display_sets(self):
        print("Number of components: ", self.num_components)
        print("Parent list:: ", end='')
        for i in range(len(self.parent)):
            print(i, ':', self.parent[i], end=', ')
        print("\nSizes : ", self.c_size)