class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        def rob_individually(val):
            if len(val) == 1:
                return val[0]
            dp = [0] * len(val)
            dp[0] = val[0]
            dp[1] = max(val[0], val[1])
            for i in range(2, len(val)):
                inc = dp[i-2] + val[i]
                exc = dp[i-1] + 0
                dp[i] = max(inc, exc)
            return dp[-1]
        start = []
        end = []
        for idx, num in enumerate(nums):
            if idx != 0:
                end.append(num)
            if idx != len(nums)-1:
                start.append(num)
        print(start)
        print(end)
        return max(rob_individually(start), rob_individually(end))

print(Solution().rob([1, 2, 3]))

