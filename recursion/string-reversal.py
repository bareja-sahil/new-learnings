def string_reversal(i, rev_str):
    n = len(rev_str) - 1
    j = n-i
    if i > j:
        return
    rev_str[i], rev_str[j] = rev_str[j], rev_str[i]
    return string_reversal(i+1, rev_str=rev_str)

rev_str = 'sahil'
i = 0

print(rev_str)
rev_str = [c for c in rev_str]
string_reversal(i, rev_str)
print(''.join(rev_str))