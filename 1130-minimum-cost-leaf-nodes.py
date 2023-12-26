import sys
from functools import lru_cache

class Solution:
    def mctFromLeafValues(self, arr):
        @lru_cache(None)
        def recur(arr):
            if len(arr) == 0:
                return 1, 0
            if len(arr) == 1:
                return arr[0], 0
            y = []
            option1 = 0
            option2 = 0
            for i in range(1, len(arr)):

                option1, min1 = recur(arr[:i])
                option2, min2 = recur(arr[i:])
                y.append((min1 + min2) + (option1 * option2))
            return max(option1, option2), min(y)
        return recur(tuple(arr))[1]
        # # print(a_dict)
        # for a,b in a_dict.items():
        #     print(f"{a}:{b}")
        # return min_sum

from timeit import default_timer as timer

start = timer()
print(Solution().mctFromLeafValues([4,3,15,7,7,13,14,9,13,8,14,13,4,13,14,1,11]))
end = timer()
print(end - start)


# print(Solution().mctFromLeafValues([6, 2, 4]

# ))