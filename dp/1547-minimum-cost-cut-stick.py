import sys


class Solution:
    def minCost(self, n, cuts):
        dp = {}

        # def solve_recursion(cuts, start, end, dp):
        #     if (start, end) in dp:
        #         return dp[(start, end)]
        #     if len(cuts) == 0:
        #         # print(x)
        #         return 0
        #     min_cost = sys.maxsize
        #
        #     for data in cuts:
        #         cost = end - start
        #         cuts_copy = cuts.copy()
        #         cuts_copy.remove(data)
        #         if start <= data <= end:
        #             left = solve_recursion(cuts_copy, start, data, dp)
        #             right = solve_recursion(cuts_copy, data, end,  dp)
        #         else:
        #             continue
        #         if left != sys.maxsize:
        #             cost += left
        #         if right != sys.maxsize:
        #             cost += right
        #         if cost == 0:
        #             return 0
        #         if cost != 0 and cost < min_cost:
        #             min_cost = cost
        #     dp[(start, end)] = min_cost
        #     return min_cost
        # return solve_recursion(cuts, 0, n, dp)
        start = 0
        end = n

        def solve(start, end, cuts):
            if len(cuts) == 0:
                return 0
            j = 0
            min_ans = sys.maxsize
            while j < len(cuts):
                new_cut = cuts[0:j] + cuts[j+1: len(cuts)+1]
                if not (start <= cuts[j] <= end):
                    j += 1
                    if j == len(cuts):
                        return 0
                    continue
                first = solve(start, cuts[j], new_cut)
                second = solve(cuts[j], end, new_cut)
                length = (end - start)
                if first == 0 and second == 0:
                    # print("1")
                    # print(length, min_ans)
                    min_ans = min(length, min_ans)
                elif first == 0:
                    # print("2")
                    # print(length, min_ans)
                    min_ans = min(length + second, min_ans)
                elif second == 0:
                    # print("3")
                    # print(length, min_ans)
                    min_ans = min(length + first, min_ans)
                else:
                    # print("4")
                    first = length + first
                    second = length + second
                    # print(first, second, length)
                    min_ans = min(first, length + second, min_ans)
                j += 1

            return solve(start, end, cuts)

        return solve(start, end, cuts)


        # def solve(start, end, cuts, cuts_ignore=[]):
        #     if len(cuts_ignore) == len(cuts):
        #         return 0
        #
        #     j = 0
        #     min_ans = sys.maxsize
        #     while j < len(cuts):
        #         if cuts[j] in cuts_ignore:
        #             j += 1
        #             continue
        #         if not (start <= cuts[j] <= end):
        #             return 0
        #
        #         # if ind == 3 and min_ans != sys.maxsize:
        #         #     print(min_ans)
        #
        #         co = cuts_ignore.copy()
        #         co.append(cuts[j])
        #         first = solve(start, cuts[j], cuts, co)
        #         second = solve(cuts[j], end, cuts, co)
        #         length = (end - start)
        #         if first == 0 and second == 0:
        #             # print("1")
        #             # print(length, min_ans)
        #             min_ans = min(length, min_ans)
        #         elif first == 0:
        #             # print("2")
        #             # print(length, min_ans)
        #             min_ans = min(length + second, min_ans)
        #         elif second == 0:
        #             # print("3")
        #             # print(length, min_ans)
        #             min_ans = min(length + first, min_ans)
        #         else:
        #             # print("4")
        #             # first = length + first
        #             # second = length + second
        #             # print(first, second, length)
        #             min_ans = min(first, length + second, min_ans)
        #         j += 1
        #     # print(f"Cuts to ignore {cuts_ignore}")
        #     # print(f"Start: {start}, end: {end}")
        #     # print(f"Mins ans: {min_ans}")
        #     # print(f"Index {ind}")
        #     return min_ans

        return solve(start, end, cuts)


# print(Solution().minCost(30, [13,25,16,20,26,5,27,8,23,14,6,15,21,24,29,1,19,9,3]
# ))
print(Solution().minCost(7, [1, 3, 4, 5]
))
