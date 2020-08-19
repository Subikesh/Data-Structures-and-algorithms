def solution1(area):
    # Your code here
    i = 1
    while i*i <= area:
        i += 1
    i -= 1
    squares = []
    while area > 0:
        if i*i <= area:
            squares.append(i*i)
            area -= i*i
        else:
            i -= 1
    return squares

import math

def get_generous(n):
    # If the numbers are in powers of 2
    return int(math.log(n, 2)+1)

def get_stingy(n):
    # if the numbers are fibonacci series
    a = b = 1
    count = 2
    summ = 2
    while summ <= n:
        c = a+b
        a, b = b, c
        summ += c
        count += 1
    count -= 1
    return count

def solution(total_lambs):
    # Your code here
    return get_stingy(total_lambs) - get_generous(total_lambs)

# a = math.log(917503, 2)
# print(bin(917503))
# print((1<<18) + (1<<18))
print(solution(917503))