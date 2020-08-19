import sys
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    min_diff = sys.maxsize
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            if abs(target - (nums[i] + nums[left]+ nums[right])) < min_diff:
                min_diff = abs(target - (nums[i] + nums[left]+ nums[right]))
                near = nums[i] + nums[left]+ nums[right]
                if min_diff == 0:
                    return near
            if (nums[i] + nums[left]+ nums[right]) <= target:
                left += 1
            elif (nums[i] + nums[left]+ nums[right]) > target:
                right -= 1
            print()
    return near

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    a = list(map(int, input().strip().split()))
    target = int(input())
    threeSumClosest(a, target)

if __name__ == '__main__':
    main()