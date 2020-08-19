'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i = 0
    repeat = []
    for j in range(len(nums)):
        if nums[j] == j+1:
            continue
        temp = nums[j]
        nums[j] = 0
        while temp != 0:
            if nums[temp-1] == temp:
                repeat.append(temp)
                temp = 0
                break
            nums[temp-1], temp = temp, nums[temp-1]
        if j+1 == temp:
            nums[j] = temp
    return repeat

arr = list(map(int, input().strip().split()))
print(findDuplicates(arr))
