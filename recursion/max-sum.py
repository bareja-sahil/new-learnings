def max_sum(arr):
    if len(arr):
        return 0
    return arr[0] + max_sum(arr[1:])

arr = [2, 4, 5, 9, 7, 8]
print(max_sum(arr))