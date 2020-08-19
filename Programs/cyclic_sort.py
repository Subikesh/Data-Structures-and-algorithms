# We are given an array containing ‘n’ objects. Each object, when created, 
# was assigned a unique number from 1 to ‘n’ based on their creation sequence.
# This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
# Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.
# For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, 
# though each number is actually an object.
# Example 1:
# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]
ar = list(map(int, input().strip().split()))

temp = ar[0]
i = temp-1
while i < len(ar):
    if i+1 == ar[i]:
        i+=1
        continue
    i = ar[temp-1]
    ar[temp-1] = temp
    temp = i
    i-=1
print(ar)