import math
import sys


class Solution:
    def numSquares(self, n):

        def recurse(n, n_sqrt, dp):
            if n == 0:
                return 0
            if n < 0:
                return sys.maxsize
            if dp[n] != -1:
                return dp[n]
            min_ans = sys.maxsize
            for i in range(1, n_sqrt+1):
                sq = int(math.pow(i, 2))
                ans = recurse(n-sq, n_sqrt, dp)
                if ans != sys.maxsize:
                    ans += 1
                    min_ans = min(min_ans, ans)
            dp[n] = min_ans
            return dp[n]
        n_sqrt = int(math.sqrt(n))
        dp = [-1] * (n + 1)
        # print(n_sqrt)
        return recurse(n, n_sqrt, dp)

print (Solution().numSquares(9))