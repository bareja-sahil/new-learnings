def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)

    return nums


def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end - 1

    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


# def partitioning(arr, start, end):
#     i = start
#     pivot = end
#     j = end - 1
#     while i <= j:
#         if i == j:
#             arr[i], arr[end] = arr[end], arr[i]
#         if arr[i] >= arr[pivot] >= arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#         if arr[i] < arr[pivot]:
#             i += 1
#         elif arr[j] > arr[pivot]:
#             j -= 1
#     return i
#
#
# def quick_sort(nums, start, end):
#     if start < end:
#         pivot = partitioning(nums, start, end)
#         quick_sort(nums, start, pivot-1)
#         quick_sort(nums, pivot+1, end)


arr = [10, 10, 10, 2, 2, 2, 0, 11, 3]
# x = partitioning(arr, 0, len(arr)-1)
# print(x)
# print(arr)
quicksort(arr)
print(arr)
