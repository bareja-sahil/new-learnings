class Solution:
    def search(self, nums, target):
        n = len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return target
        if len(nums) == 1 and nums[0] != target:
            return -1

        def binary_search(arr, start, end, key):
            mid = (start + end) // 2
            if start > end:
                return -1
            if nums[mid] == key:
                return mid
            if nums[mid] > key:
                return binary_search(arr, start, mid-1, key)
            else:
                return binary_search(arr, mid+1, end, key)

        def find_pivot(start, end, nums):
            while start < end:
                mid = (start + (end)) // 2
                if nums[mid] >= nums[0]:
                    start = mid + 1
                else:
                    end = mid
            return start

        pivot = find_pivot(0, n, nums)
        if nums[0] <= target <= nums[pivot-1]:
            return binary_search(nums, 0, pivot-1, target)
        else:
            return binary_search(nums, pivot, n, target)

print(Solution().search([1, 3], 1))
