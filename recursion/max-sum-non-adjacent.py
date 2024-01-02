def max_sum(nums):
    max_non_adj = -1

    def recurse(nums, i, target):
        nonlocal max_non_adj
        if i >= len(nums):
            # print(target)
            max_non_adj = max(target, max_non_adj)
            return
        recurse(nums, i+2, target+nums[i])
        recurse(nums, i+1, target)
    recurse(nums, 0, 0)
    print(max_non_adj)


def max_sum_dp(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)+1):
        inc = recurse(nums, i + 2, dp) + nums[i]
        exc = recurse(nums, i + 1, dp) + 0
        dp[i] = max(inc, exc)

def max_sum_memo(nums):
    dp = [-1] * len(nums)

    def recurse(nums, i, dp):
        if i >= len(nums):
            # print(target)
            return 0
        if dp[i] != -1:
            return dp[i]
        inc = recurse(nums, i+2, dp) + nums[i]
        exc = recurse(nums, i+1, dp) + 0
        dp[i] = max(inc, exc)
        return dp[i]
    return recurse(nums, 0, dp)
    # print(max_non_adj)
from timeit import default_timer as timer

start = timer()
print(max_sum_memo([9, 9, 8, 2]))
end = timer()
print(end - start)

start = timer()
print(max_sum([9, 9, 8, 2]))
end = timer()
print(end - start)

