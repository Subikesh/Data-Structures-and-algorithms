# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n!n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.

def is_pattern_present(s2, s1):
    
    if len(s1) > len(s2):
        return False
    patt = {}
    for i in s1:
        patt[i] = patt.get(i, 0) + 1
    # print(patt)
    match = 0
    for i in range(len(s1)):
        if s2[i] in patt:
            patt[s2[i]] -= 1
            if patt[s2[i]] == 0:
                match += 1
        # print(patt, match)
    if match == len(patt):
        return True

    start = 0
    for i in range(len(s1), len(s2)):
        if s2[start] in patt:
            if patt[s2[start]] == 0:
                match -= 1            
            patt[s2[start]] += 1            
        if s2[i] in patt:
            patt[s2[i]] -= 1
            if patt[s2[i]] == 0:
                match += 1
        start += 1
        if match == len(patt):
            return True
    return False


s2 = input()
s1 = input()
print(is_pattern_present(s2, s1))