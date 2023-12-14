def dynamic_programing_lcs(seq1, seq2):
    table = [[0 for i in range(len(seq2)+1)] for j in (range(len(seq1)+1))]
    for idx1 in (range(len(seq1))):
        for idx2 in (range(len(seq2))):
            if seq1[idx1] == seq2[idx2]:
                table[idx1+1][idx2+1] = 1 + table[idx1][idx2]
            else:
                table[idx1 + 1][idx2 + 1] = max(table[idx1+1][idx2], table[idx1][idx2+1])

    return table[-1][-1]



seq1 = 'ate'
seq2 = ''
print(dynamic_programing_lcs(seq1, seq2))