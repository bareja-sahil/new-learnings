import sys


class Solution:
    def searchRange(self, nums, target):
        start_key = -1
        end_key = -1
        if len(nums) == 0:
            return -1, -1
        if len(nums) == 1 and target == nums[0]:
            return 0, 0
        elif len(nums) == 1 and target != nums[0]:
            return -1, -1

        def firstOccurance(nums, start, end, key):
            nonlocal start_key
            if start > end:
                return
            mid = (start + end) // 2
            if nums[mid] == key:
                start_key = mid
                if mid > 0 and nums[mid - 1] == key:
                    return firstOccurance(nums, start, mid - 1, key)
            if nums[mid] > key:
                return firstOccurance(nums, start, mid - 1, key)
            elif nums[mid] < key:
                return firstOccurance(nums, mid + 1, end, key)

        def lastOccurance(nums, start, end, key):
            nonlocal end_key
            ans = -1
            if start > end:
                return
            mid = (start + end) // 2
            if nums[mid] == key:
                end_key = mid
                if mid < len(nums) - 1 and nums[mid + 1] == key:
                    return lastOccurance(nums, mid + 1, end, key)
            if nums[mid] > key:
                return lastOccurance(nums, start, mid - 1, key)
            elif nums[mid] < key:
                return lastOccurance(nums, mid + 1, end, key)

        firstOccurance(nums, 0, len(nums) - 1, target)
        lastOccurance(nums, 0, len(nums) - 1, target)
        return start_key, end_key


print(Solution().searchRange([3,3,3]
, 3))