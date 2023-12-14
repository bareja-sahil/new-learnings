profits = [1, 3, 3]
weights = [1, 2, 3]
capacity = 3


def max_profit(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    if weights[idx] > capacity:
        return max_profit(weights, profits, capacity, idx+1)
    else:
        options1 = max_profit(weights, profits, capacity, idx+1)
        options2 = profits[idx] + max_profit(weights, profits, capacity-weights[idx], idx+1)
        if options2 > options1:
            print([idx])
        return max(options1, options2)


print(max_profit(weights, profits, capacity))
