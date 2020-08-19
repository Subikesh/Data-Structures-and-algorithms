'''
You are given a string. You need to print the lexicographically sorted power-set of the string.
Note: The string s contains lowercase letter of alphabet.
'''
def find_sets(s, l, char, sets):    
    if l == len(s):
        print(sets, char)
        sets.append(char)
    else:
        find_sets(s, l+1, char+s[l], sets)

        find_sets(s, l+1, char, sets)

def powerSet(s):
    '''
    :param s: given string s
    :return: list containing power set of s.
    '''
    sets = []
    find_sets(s, 0, '', sets)
    return sets

#{ 
#  Driver Code Starts
#Initial Template for Python 3
# import atexit
# import io
# import sys

# #Contributed by : Nagendra Jha

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register

# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        s = str(input())
        ans = powerSet(s)
        ans.sort()
        print(*ans)
# } Driver Code Ends