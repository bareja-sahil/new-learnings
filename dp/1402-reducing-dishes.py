class Solution:
    def maxSatisfaction(self, satisfaction):
        n = len(satisfaction)
        satisfaction = sorted(satisfaction)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        # for i in range(1,  n+1):
        #     ans = 0
        #     for j in range(1,  n+1):
        #         print(i, j)
        #         inc = satisfaction[i-1] * (j) + dp[i - 1][j - 1]
        #         exc = 0 + dp[i - 1][j]
        #         if exc == 0:
        #             ans = inc
        #         else:
        #             ans = max(inc, exc)
        #         dp[i][j] = ans
        for i in range(n-1,  -1, -1):
            ans = 0
            for j in range(n-1, -1, -1):
                print(i, j)
                inc = satisfaction[i] * (j) + dp[i + 1][j + 1]
                exc = 0 + dp[i + 1][j]

                ans = max(inc, exc)
                dp[i][j] = ans
        print(dp)
        # def solve(satisfaction, index, time, dp):
        #     if (index, time) in dp:
        #         return dp[(index, time)]
        #     if index == len(satisfaction):
        #         return 0
        #     inc = satisfaction[index] * (time + 1) + solve(satisfaction, index + 1, time + 1, dp)
        #     exc = 0 + solve(satisfaction, index + 1, time, dp)
        #     ans = max(inc, exc)
        #     dp[(index, time)] = ans
        #     return ans
        #
        # satisfaction.sort()
        # return solve(satisfaction, 0, 0, dp)

Solution().maxSatisfaction([-1,-8,0,5,-9])
# Solution().maxSatisfaction([-1,0,5])
