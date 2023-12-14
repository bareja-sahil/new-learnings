def knap_sack_dp(weights, profits, capacity):
    table = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for i in range(len(weights)):
        for c in range(1, capacity+1):
            if weights[i] > c:
                table[i+1][c] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], profits[i]+table[i][c-weights[i]])
    print(table)
    return table[-1][-1]


capcity = 3
weights = [1, 3, 3, 2]
profits = [1, 3, 3, 6]

print(knap_sack_dp(weights, profits, capcity))