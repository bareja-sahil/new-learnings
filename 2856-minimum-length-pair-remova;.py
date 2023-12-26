def find_minimum_length_pair(nums):
    end = len(nums)
    idx1 = 0
    mid = (0 + end) // 2
    idx2 = mid
    result = 0
    while idx1 < mid and idx2 < end:
        if nums[idx1] < nums[idx2]:
            idx1 += 1
            idx2 += 1
        else:
            result += 1
            idx2 += 1
    result += (mid-idx1) + (end - idx2)
    return result

print(find_minimum_length_pair([1,2, 2]))