import sys
class Solution:
    def maxProfit(self, prices):
        result  = 0
        if len(prices) == 1:
            return result
        min = prices[0]
        max = prices[0]
        for idx, num in enumerate(prices):
            if num < min:
                min = num
                max = num
            elif num >= max:
                max = num
        if max - min > 0:
            return max-min
        else:
            return 0
print(Solution().maxProfit([7,6,4,3,1]))

