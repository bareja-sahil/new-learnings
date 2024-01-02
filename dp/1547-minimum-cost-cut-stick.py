import sys


class Solution:
    def minCost(self, n, cuts):
        cuts.sort()

        def solve_recursion(cuts, start, end, x=1):
            if len(cuts) == 0:
                print(x)
                return 0
            cost = end-start

            min_cost = sys.maxsize
            left = sys.maxsize
            right = sys.maxsize
            for data in cuts:
                cuts_copy = cuts.copy()
                cuts_copy.remove(data)
                print(f"data: {data}")
                print(x)
                if start <= data <= end:
                    left = solve_recursion(cuts_copy, start, data, x+1) + cost
                    right = solve_recursion(cuts_copy, data, end,  x+1) + cost
                cost = min(left, right)
                print(f"cost: {cost}")
                if cost < min_cost:
                    min_cost = cost
            return min_cost
        return solve_recursion(cuts, 0, n)


print(Solution().minCost(7, [1, 3, 4, 5]))
