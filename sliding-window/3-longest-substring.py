def longest_substring(s):
    sub_dict = {}
    max_target = 0
    target = 0
    for ch in s:
        if sub_dict.get(ch, 0) == 0:
            target += 1
            sub_dict[ch] = 1
        else:
            max_target = max(max_target, target)
            target = 0
            sub_dict = {}
            sub_dict[ch] = 1
            target += 1
    max_target = max(max_target, target)
    return max_target

# print(longest_substring("abcabcbb"))
# print(longest_substring("bbbbb"))
print(longest_substring("dvdf"))