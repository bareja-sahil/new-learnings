class Solution:
    def findTargetSumWays(self, nums, target) :
        def recurse(nums, target, target_sum, index):
            if (target == target_sum) and index == len(nums):
                return 1
            if index == len(nums):
                return 0
            if (index, target_sum) in dp:
                return dp[(index, target_sum)]
            ans = recurse(nums, target, target_sum + nums[index], index + 1) + recurse(nums, target,
                                                                                       target_sum - nums[index],
                                                                                       index + 1)
            dp[index, target_sum] = ans
            return dp[index, target_sum]

        return recurse(nums, target, 0, 0)
