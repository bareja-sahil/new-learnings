def len_lcs(seq1, seq2, idx1, idx2):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        idx1 += 1
        idx2 += 1
        return 1 + len_lcs(seq1, seq2, idx1, idx2)
    else:
        inc_idx1 = idx1 + 1
        inc_idx2 = idx2 + 1
        return max(len_lcs(seq1, seq2, inc_idx1, idx2), len_lcs(seq1, seq2, idx1, inc_idx2))


print(len_lcs(' ', '', 0, 0))
