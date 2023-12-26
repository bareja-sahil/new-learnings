def is_sorted(arr, size):
    if size == 0 or size == 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted(arr[1:], size-1)


arr = [2, 4, 5, 9, 7, 8]
print(is_sorted(arr, len(arr)))