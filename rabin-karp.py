def get_hash(pat):
    size = len(pat)
    val = 0
    for i in range(size):
        val += ord(pat[i]) * 26**(size-i-1)
    return val

def rabin_karp(stri, pat):
    pat_hash = get_hash(pat)
    pat_size = len(pat)
    str_hash = get_hash(stri[:pat_size])
    matched = []
    if str_hash == pat_hash:
        matched.append(i)
    for i in range(1, len(stri)-pat_size+1):
        last_hash = ord(stri[i-1])*(26**(pat_size-1))
        str_hash = (str_hash - last_hash)*26 + ord(stri[i+pat_size-1])
        if str_hash == pat_hash:
            matched.append(i)
    return matched

print(rabin_karp("ABAACAADAABAABA", "AABA"))
