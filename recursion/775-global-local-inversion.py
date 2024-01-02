def global_local_inversion(nums):
    global_inversion = 0
    local_inversion = 0
    for i in range(0,len(nums) - 1):
        if nums[i] > nums[i + 1]:
            local_inversion += 1
        if local_inversion > 1:
            return False

    def merge(left, right):
        nonlocal global_inversion
        swapped = True
        i = 0
        j = 0
        final = []
        first = len(left)
        second = len(right)
        while i < first and j < second:
            if left[i] < right[j]:
                final.append(left[i])
                i += 1
            else:
                global_inversion += first - i
                final.append(right[j])
                j += 1
        return final + right[j:] + left[i:]

    def merge_sort(arr, start, end):

        if start > end:
            return
        if start == end:
            return [arr[start]]
        mid = (start + end) // 2
        left = merge_sort(arr, start, mid)
        right = merge_sort(arr, mid + 1, end)

        return merge(left, right)

    merge_sort(nums, 0, len(nums) - 1)
    print(local_inversion)
    print(global_inversion)
    return local_inversion == global_inversion

arr = [1, 0]
print(global_local_inversion(arr))