# Given an array arr[] of N non-negative integers representing the height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
# The structure is like below:
# | |
# |_|
# We can trap 2 units of water in the middle gap.

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if height == []:
        return 0
    left = 0
    right = len(height)-1
    max_left = height[left]
    max_right = height[right]
    vol = 0
    while left < right:
        if height[left] <= height[right]:
            max_left = height[left] if height[left] > max_left else  max_left
            vol += max_left - height[left]
            left += 1
        else:
            max_right = height[right] if height[right] > max_right else  max_right
            vol += max_right - height[right]
            right -= 1
    return vol

arr = list(map(int, input().strip().split()))
print(trappingWater(arr, len(arr)))
# The solution is wrong