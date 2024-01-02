class Solution:
    def minCostClimbingStairs(self, cost):

        if len(cost) < 2:
            return min(cost)
        prev2 = cost[0]
        prev1 = cost[1]
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr
        return min(prev1, prev2)

print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))