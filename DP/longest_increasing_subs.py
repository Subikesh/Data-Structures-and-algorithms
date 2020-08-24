"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
"""

# The solution is done using dynamic programming - https://leetcode.com/problems/longest-increasing-subsequence/solution/
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    dp = [1]
    for i in range(1,len(nums)):
        maxx = 0
        for j in range(i):
            if nums[j] < nums[i]:
                maxx = max(maxx, dp[j])
        dp.append(maxx+1)
    return max(dp)

nums = list(map(int, input().strip().split()))
print(lengthOfLIS(nums))