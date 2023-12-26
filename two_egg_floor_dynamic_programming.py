import sys


def two_egg_floor_dp(n):
    eggs = 2
    result = [0] * (eggs+1)
    for i in range(eggs+1):
        result[i] = [0] * (n+1)
    # print(result)
    for i in range(1, 3):
        result[i][0] = 0
        result[i][1] = 1
    for i in range(1, n+1):
        result[1][i] = i
    # print(result)
    for j in range(2, n+1):
        result[2][j] = sys.maxsize
        for x in range(1, j+1):
            min_result = 1 + max(result[1][x-1], result[2][j-x])
            if min_result < result[2][j]:
                result[2][j] = min_result
    print(result)
    return result[-1][-1]

print(two_egg_floor_dp(100))