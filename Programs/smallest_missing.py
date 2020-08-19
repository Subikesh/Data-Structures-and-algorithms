# Smallest Positive missing number 
# You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.
# Note: Expected solution in O(n) time using constant extra space.

def findMissing(arr, size): 
    # your code goes here
    for i in range(size):
        if arr[i] < 0:
            arr[i] = 0
    for i in range(size):
        if arr[i] != 0 or i == arr[i]-1:
            temp = arr[i]
            arr[i] = 0
            while arr[temp-1] != 0:
                arr[temp-1], temp  = temp, arr[temp-1]
            arr[temp-1] = temp
    for i in range(size):
        if arr[i] == 0:
            return i+1
    else:
        return size+1

li = list(map(int, input().strip().split()))
print(findMissing(li, len(li)))