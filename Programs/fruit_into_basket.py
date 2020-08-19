class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        start = 0
        max_count = 2
        while start < len(tree):
            tree_count = 0
            # b1 and b2 assignment
            b1 = tree[start]
            while start < len(tree) and tree[start] == b1:
                start +=1
                tree_count += 1
            if start == len(tree):
                break
            b2 = tree[start]
            while start < len(tree) and tree[start] in [b1, b2]:
                tree_count += 1
                start += 1
            max_count = max(tree_count, max_count)
            start -= 1
        return max_count

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            # line = lines.next()
            # tree = stringToIntegerList(line)
            tree = list(map(int, input().strip().split()))
            ret = Solution().totalFruit(tree)

            out = intToString(ret)
            print (out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()