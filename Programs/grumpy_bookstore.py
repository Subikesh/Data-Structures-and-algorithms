def maxSatisfied(customers, grumpy, X):
    """
    :type customers: List[int]
    :type grumpy: List[int]
    :type X: int
    :rtype: int
    """
    sum_cust = 0
    count = 0
    start = 0
    for i in range(len(customers)):
        if grumpy[i] == 0:
            sum_cust += customers[i]
    win = sum_cust
    if X == 0:
        return sum_cust
    for i in range(X):
        if grumpy[i] == 1:
            count += 1
            win += customers[i]
    sum_cust = max(sum_cust, win)
    for i in range(X, len(customers)):
        if grumpy[i] == 1:
            win += customers[i]
            count += 1
        if grumpy[start] == 1:
            win -= customers[start]
            count -= 1
        start += 1
        if count > X:
            continue
        sum_cust = max(win, sum_cust)
    return sum_cust

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    cust = list(map(int, input().strip().split()))
    grum = list(map(int, input().strip().split()))
    X = int(input())
    print(maxSatisfied(cust, grum, X))

if __name__ == '__main__':
    main()