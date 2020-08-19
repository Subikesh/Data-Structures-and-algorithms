"""
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""

# Doing by tree implementation
class Node:
    def __init__(self):
        self.value = 0
        self.count = 0
        self.lcount = 0
        self.left = None
        self.right = None
    
def create_node(nval, ncnt):
    nnode = Node()
    nnode.value = nval
    nnode.count = ncnt
    nnode.lcount = 0
    return nnode

def get_small_count(nums):
    count = [0 for i in nums]
    root = create_node(nums[-1], 0)
    for i in range(len(nums)-2, -1, -1):
        ptr = root
        nnode = create_node(nums[i], 0)
        while True:
            if ptr.value < nums[i]:
                nnode.count += ptr.lcount +1
                if ptr.right != None:   ptr = ptr.right
                else:   
                    ptr.right = nnode
                    break
            else:
                ptr.lcount += 1
                # nnode.count += ptr.lcount
                if ptr.left != None:   ptr = ptr.left
                else:   
                    ptr.left = nnode
                    break
        count[i] = nnode.count
    return count

if __name__ == "__main__":
    nums = list(map(int, input().rstrip().split()))
    print(get_small_count(nums))