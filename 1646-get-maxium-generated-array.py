class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        max_num = 1
        half = int(n / 2)
        nums[0], nums[1] = 0, 1
        for i in range(1, half + 1):
            x = nums[i]
            max_num = x if x > max_num else max_num
            nums[2 * i] = x
            try:
                y = nums[i] + nums[i + 1]
                nums[2 * i + 1] = y
                max_num = y if y > max_num else max_num
            except IndexError as ie:
                break
        return max_num

print(Solution().getMaximumGenerated(3))