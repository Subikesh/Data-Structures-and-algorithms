def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    sum_target = []
    first = 0
    while first < len(nums)-3:
        sec = first + 1
        while sec < len(nums)-2:
            third = sec+1
            fourth = len(nums)-1
            while third < fourth:
                sum_ptr = nums[first] + nums[sec]+ nums[third]+ nums[fourth]
                if sum_ptr == target:
                    sum_target.append([nums[first], nums[sec], nums[third], nums[fourth]])
                    # third += 1
                if sum_ptr < target:
                    prev = nums[third]
                    while third < fourth and nums[third] == prev:
                        third += 1
                if sum_ptr >= target:
                    prev = nums[fourth]
                    while third < fourth and nums[fourth] == prev:
                        fourth -= 1
            prev = nums[sec]
            while sec < len(nums)-2 and prev == nums[sec]:
                sec += 1
        prev = nums[first]
        while first < len(nums)-3 and prev == nums[first]:
            first += 1
    return sum_target

def main():
    nums = list(map(int, input().strip().split()))
    target = int(input())
    print(fourSum(nums, target))

if __name__ == '__main__':
    main()