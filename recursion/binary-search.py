def binary_search(arr, start, end, key):
    mid = (start + end) // 2
    if start > end:
        return False
    if arr[mid] == key:
        return True
    if arr[mid] > key:
        return binary_search(arr, start, mid-1, key)
    else:
        return binary_search(arr, mid+1, end, key)


arr = [2, 5, 6, 7, 10, 13, 34, 56]
print(binary_search(arr, 0, len(arr), 5))