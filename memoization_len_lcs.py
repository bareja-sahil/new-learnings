def memoization_len_lcs(seq1, seq2):
    memo = dict()

    def recursi(idx1, idx2):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif len(seq1) == idx1 or len(seq2) == idx2:
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recursi(idx1+1, idx2+1)
        else:
            memo[key] = max(recursi(idx1+1, idx2), recursi(idx1, idx2+1))
        return memo[key]
    return recursi(0, 0)


print(memoization_len_lcs('ate', 'cate'))