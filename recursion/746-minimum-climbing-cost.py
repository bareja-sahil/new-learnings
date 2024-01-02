class Solution:
    def minCostClimbingStairs(self, cost):
        cost_map = {}

        def recurse(cost, n):
            if n in cost_map:
                return cost_map[n]
            if n <= 1:
                return cost[n]
            x = cost[n] + min(recurse(cost, n-2), recurse(cost, n-1))
            cost_map[n] = x
            return x
        cost.append(0)
        return recurse(cost, len(cost)-1)

print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))