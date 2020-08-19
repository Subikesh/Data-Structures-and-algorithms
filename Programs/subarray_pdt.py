def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    left, right = 0, 0
    count = 0
    prod = 1
    if k <= 1: return 0
    while right < len(nums):
        prod *= nums[right]
        # if prod < k:
        #     count +=1
        while prod >=k:
            prod = prod // nums[left]
            left += 1
        count += right - left + 1
        right += 1
    return count


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
    K =  int(input())
    print(numSubarrayProductLessThanK(a, K))

if __name__ == '__main__':
    main()