def characterReplacement(A, K):
    """
    :type A: str
    :type K: int
    :rtype: int
    """
    dicts = {}
    start = 0
    max_val = 0
    i = -1 
    for i in range(len(A)):
        if not dicts.get(A[i], 0):
            dicts[A[i]] = 1
        else:
            dicts[A[i]] += 1
        if len(dicts) > 0:
            m_dic = max(dicts.values())
            s_dic = sum(dicts.values())
        while s_dic - m_dic > K:
            max_val = (i-start) if (i-start)>max_val else max_val
            dicts[A[start]] -= 1
            start += 1
            m_dic = max(dicts.values())
            s_dic -= 1
        print()
    max_val = (i-start+1) if (i-start+1)>max_val else max_val
    return max_val

def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    # lines = readlines()
    # while True:
    #     try:
    #         line = lines.next()
    #         s = stringToString(line)
    #         line = lines.next()
    #         K = stringToInt(line)
            
    #         ret = Solution().characterReplacement(s, K)

    #         out = intToString(ret)
    #         print out
    #     except StopIteration:
    #         break
    s = input()
    K = int(input())
    print(characterReplacement(s, K))

if __name__ == '__main__':
    main()