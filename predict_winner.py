"""
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

"""
def PredictTheWinner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) <= 2:
        return True
    return score(nums, 0, 0, True)
    
    
def score(nums, f, s, first_person):
    if len(nums) == 2:
        # When the length is 2, then f takes the maximum element and s takes the other
        # Then, if their score after that, is the same, then the first player(global first call) wins
        if f+max(nums) == s+min(nums):
            return True if first_person else False
    if len(nums) == 0:
        if f < s:
            return False
        else:
            return True
    
    if not self.score(nums[1:], s, f+nums[0], not first_person):
        return True
    if not self.score(nums[:-1], s, f+nums[-1], not first_person):
        return True
    
    return False
        
nums = list(map(int, input().strip().split()))
print(PredictTheWinner(nums))