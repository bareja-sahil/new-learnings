def bubble_sort(arr, n):
    if n == 0 or n == 1:
        return arr
    i = 0
    while i < n-1:
        if arr[i] >= arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 1
    bubble_sort(arr, n-1)

arr = [3, 2, 5, 88, 33, 21, 12, 4, 4, 5, 5, 6, 6]
bubble_sort(arr, 13)
print(arr)