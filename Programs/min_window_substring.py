
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s) < len(t):
        return ""
    if len(s) == 1:
        if s != t:
            return ""
        else:
            return s
    patt = {}
    for i in t:
        patt[i] = patt.get(i, 0) + 1
    start = 0
    match = 0
    min_index = [0, len(s)+1]
    while start < len(s) and s[start] not in patt:
        start += 1
    if start == len(s):
        return ""
    for i in range(start, len(s)):
        if s[i] in patt:
            patt[s[i]] -= 1
            if patt[s[i]] == 0:
                match += 1
        if patt.get(s[start], None) == -1:
            patt[s[start]] += 1
            # if match == len(patt):
            #     match -= 1
            start += 1
            while s[start] not in patt:
                start += 1
        if match == len(patt):
            if match == len(patt):
                min_index = ([start, i+1]) if (i+1-start) < min_index[1] - min_index[0] else min_index
            # print(min_index, start, i)
            while start <= i:
                if s[start] in patt:
                    patt[s[start]] += 1
                    if match == len(patt):
                        match -= 1
                start += 1
                if start >= len(s) or s[start] in patt:
                    break
    if min_index[1] - min_index[0] == len(s)+1:
        return ""
    return s[min_index[0]:min_index[1]]
    
def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    a = input()
    b = input()
    print(minWindow(a, b))

if __name__ == '__main__':
    main()