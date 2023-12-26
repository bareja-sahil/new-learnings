class Solution:
    def twoSum(self, numbers, target):
        for idx, i in enumerate(numbers):
            remainder = target-i
            if remainder in numbers:
                index = numbers.index(remainder)
                return [idx+1, index+1]
print(Solution().twoSum([2,7,11,15], target = 9))
