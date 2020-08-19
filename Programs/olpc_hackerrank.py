import math
def isprime(n):
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+2):
        if n%i == 0:
            return False
    return True

def find_classroom(n):
    for i in range(2, n+1):
        if n%i == 0 and isprime(i):
            return i

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def rounded(n):
    sums = []
    while n >= 0:
        rem = n%10
        n //= 10
        if rem != 0:
            sums.append(rem)
    return reversed(sums)

def move_fast(x, y, k):
    if k == x or k == y:
        return 0
    move = []
    mid = (x+y)//2
    if k > mid:
        move.append(move_fast(mid, y, k))
        move.append(y-k)
    else:
        move.append(move_fast(x, mid, k))
        move.append(k-x)
    return min(move)

def count_lines(lines):
    lines.sort(key=lambda x: x[0])
    count = 1
    beg = lines[0][0]
    end = lines[0][1]
    for line in lines:
        if line[0]>end:
            count += 1
            beg = line[0]
            end = line[1]
        else:
            end = min(end, line[1])
            beg = max(beg, line[0])
    return count

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# Using seive of erasthanos to get all prime numbers till n
def get_primes(n):
    primes = [True for i in range(n)]
    for i in range(2, int(math.sqrt(n))+2):
        if primes[i-1]:
            j = i**2
            while j <= n:
                primes[j-1] = False
                j += i
    result = []
    for i in range(1, len(primes)):
        if primes[i]:
            result.append(i+1)
    return result

# 1, 4, 3, 8, 6
def remove_students(stud):
    primes = get_primes(max(stud))
    maxx = max(stud)
    freq = {}
    for p in primes:
        freq[p] = 0

    for prime in freq:        
        for i in range(len(stud)):
            if stud[i]%prime == 0:
                freq[prime] += 1
    return n - max(freq.values())