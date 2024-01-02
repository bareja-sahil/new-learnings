import sys


def min_coin_sum(coins, sum):
    suns_array = [sys.maxsize] * (sum + 1)
    suns_array[0] = 0
    for min_sum in range(1, len(suns_array)):
        for coin in coins:
            if min_sum-coin >= 0 and suns_array[min_sum-coin] != sys.maxsize:
                suns_array[min_sum] = min(suns_array[min_sum], 1 + suns_array[min_sum-coin])
    print(suns_array)

min_coin_sum([3, 3], 5)