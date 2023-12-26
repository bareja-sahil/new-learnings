class Solution:
    def countArrangement(self, n):
        array = [x for x in range(1, n + 1)]
        self.res = 0

        # def check(array):
        #     for i, n in enumerate(array):
        #         i = i+1
        #         if (n % i) == 0 or (i % n) == 0:
        #             pass
        #         else:
        #             return
        #     self.res += 1
        def dfs(array, x, z):
            if x > n:
                self.res += 1
            for i, j in enumerate(array):
                if (j % x) == 0 or (x % j) == 0:

                    dfs(array[:i] + array[i + 1:], x+1, z + [j])
                    # self.res += 1

            # print('\n')

        dfs(array, 1, [])
        return self.res

print(Solution().countArrangement(4))
