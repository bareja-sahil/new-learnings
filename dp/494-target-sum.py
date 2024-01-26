class Solution:
    def findTargetSumWays(self, nums, target) :
        dp =[[-1 for j in range(target+1)] for i in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = 0
        for j in range(target + 1):
            dp[0][j] = 0
        print(dp)
        for i in range(1, target+1):
            for j in range(1, len(nums)+1):
                dp[i][j] = dp[i][j]

        # def recurse(nums, target, target_sum, index):
        #     if (target == target_sum) and index == len(nums):
        #         return 1
        #     if index == len(nums):
        #         return 0
        #     if (index, target_sum) in dp:
        #         return dp[(index, target_sum)]
        #     ans = recurse(nums, target, target_sum + nums[index], index + 1) + recurse(nums, target,
        #                                                                                target_sum - nums[index],
        #                                                                                index + 1)
        #     dp[index, target_sum] = ans
        #     return dp[index, target_sum]
        #
        # return recurse(nums, target, 0, 0)


Solution().findTargetSumWays([1,1,1,1,1], 3)