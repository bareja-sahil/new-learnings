import math
import sys


class Solution:
    def numSquares(self, n):
        n_sqrt = int(math.sqrt(n))
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            min_ans = sys.maxsize
            for j in range(1, n_sqrt+1):
                sq = int(math.pow(j, 2))
                if i-sq >= 0:
                    ans = dp[i-sq] + 1
                    min_ans = min(min_ans, ans)
            dp[i] = min_ans
        return dp[n]

print (Solution().numSquares(99))