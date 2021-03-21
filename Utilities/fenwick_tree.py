'''
Fenwick tree(Binary indexed tree) is a data structure used to make range queries easily: https://youtu.be/RgITNht_f4Q
We can use prefix-sum array to do this in O(1). But updation of array takes O(n)
Instead we use Fenwick tree: 
    Construction : O(n)
    Point update : O(log(n))
    Range sum : O(log(n)) 
    Range update : O(log(n)) 
    Adding and removing elements to array not possible
'''

class FenwickTree:

    # Construct a Fenwick tree with an initial set of values.
    # The 'values' array MUST BE ONE BASED meaning values[0]
    # does not get used, O(n) construction.
    def __init__(self, values=None):
        if values is None:
            raise ValueError("Values array cannot be Null")
        values[0] = 0
        self.tree = values.deepcopy()

        # Adding the values to the tree's parents - https://youtu.be/BHPez138yX8
        for i in range(1, len(values)):
            parent = i + self.lsb(i)
            if parent < N:
                self.tree[parent] += self.tree[i]
