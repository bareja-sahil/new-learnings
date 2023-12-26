def aggressive_cows(nums, k):
    nums = sorted(nums)

    def is_possible(nums, k, mid):
        stalls = 1
        initial_cow = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - initial_cow >= mid:
                initial_cow = nums[i]
                stalls += 1
        return stalls >= k

    start = nums[1]
    end = nums[-1]
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if is_possible(nums, k, mid):
            start = mid+1
            res = mid
        else:
            end = mid-1
    return res


print(aggressive_cows([0, 3, 4, 7, 10, 9], 4))
