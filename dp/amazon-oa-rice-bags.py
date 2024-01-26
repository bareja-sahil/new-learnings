def rice_bags(nums):
    nums.sort()
    max_ans = -1
    n = len(nums)
    dp = [[0 for i in range(len(nums)+1)] for j in range(len(nums)+1)]
    print(dp)
    for i in range((n-1), -1, -1):
        for j in range((n-1), -2, -1):
            inc = 0
            if j == -1 or nums[j] * nums[j] == nums[i]:
                inc = 1 + dp[i + 1][i+1]
            exc = 0 + dp[i+1][j+1]
            dp[i][j+1] = max(inc, exc)

    print(dp)
    return dp[0][0]
    # def solve(nums, prev_index, index, dp):
    #     if index == len(nums):
    #         return 0
    #     if dp[index][prev_index] != -1:
    #         return dp[index][prev_index]
    #     inc = 0
    #     if prev_index == -1 or nums[prev_index] * nums[prev_index] == nums[index]:
    #         inc = 1 + solve(nums, index, index+1, dp)
    #     exc = 0 + solve(nums, prev_index, index+1, dp)
    #     dp[index][prev_index] = max(inc, exc)
    #     return dp[index][prev_index]
    # return solve(nums, -1, 0, dp)


print(rice_bags([3, 4, 2, 9, 81]))