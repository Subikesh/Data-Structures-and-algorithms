def circularArrayLoop( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def move(i):
        res = (i+nums[i])%len(nums)
        return res
    slow = move(0)
    fast = move(slow)
    while slow != fast:
        slow = move(slow)
        fast = move(move(fast))
    fast = move(slow)
    if fast == slow:    return False
    if nums[slow]>0:
        while fast != slow:
            fast = move(fast)
            if nums[fast]<0:    return False
    else:
        while fast != slow:
            fast = move(fast)
            if nums[fast] > 0:  return False
    return True

def stringToIntegerList(input):
    return json.loads(input)

def main():
    nums = list(map(int, input().strip().split()))
    print(circularArrayLoop(nums))

if __name__ == '__main__':
    main()