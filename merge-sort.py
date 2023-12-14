def merge_sort(left, right):
    i, j = 0, 0
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list


def divide_list(list, lo=0, hi=None):
    if hi is None:
        hi = len(list) - 1
    if lo == hi:
        return [list[lo]]
    mid = (lo + hi) // 2
    left_list = divide_list(list, lo, hi=mid)
    right_list = divide_list(list, mid+1, hi=hi)
    return merge_sort(left_list, right_list)
#
# x = [2, 4]
# y = [3, 9]
# print(merge_sort(x, y))
list = [3, 5, 66, 777, 22, 12, 33]
print(divide_list(list))