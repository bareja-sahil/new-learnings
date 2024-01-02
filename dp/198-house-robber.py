class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            inc = dp[i - 2] + nums[i]
            exc = dp[i - 1] + 0
            dp[i] = max(inc, exc)
        return dp[-1]

Solution().rob([1,2,3,1])
