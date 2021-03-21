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
    
    # Returns the value of the least significant bit (LSB)
    # lsb(108) = lsb(0b1101100) =     0b100 = 4
    # lsb(104) = lsb(0b1101000) =    0b1000 = 8
    # lsb(96)  = lsb(0b1100000) =  0b100000 = 32
    # lsb(64)  = lsb(0b1000000) = 0b1000000 = 64
    def LSB(self, i):
        return i & -i

    # Computes the prefix sum from [1, i], O(log(n))
    def prefix_sum(self, i):
        sum = 0
        while i != 0:
            sum += self.tree[i]
            i &= ~self.lsb(i) # Same as i -= lsb(i)
        return sum

    # Returns the sum of the interval [left, right], O(log(n))
    def sum(self, left, right):
        if right < left:
            raise ValueError("Right must be >= Left")
        return self.prefix_sum(right) - self.prefix_sum(left-1)
    
    # Return the value in that index and not sum
    def get(self, i):
        return self.sum(i, i)

    # Add 'v' to index 'i', O(log(n))
    def add(self, i, v):
        while (i < len(self.tree)):
            self.tree[i] += v
            i += self.lsb(i)    

    # Set index i to be equal to v, O(log(n))
    def set(self, i, v):
        self.add(i, v - self.get(i))

