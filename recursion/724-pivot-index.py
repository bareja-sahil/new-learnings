class Solution:
    def pivotIndex(self, nums):
        n = len(nums) - 1
        main_start = 0
        end_start = len(nums)

        def binary_serach(arr, start, end):
            nonlocal main_start
            nonlocal end_start
            mid = (start + end) // 2
            left_sum = sum(arr[main_start:mid])
            right_sum = sum(arr[mid+1:end_start])
            if start > end:
                return -1
            if left_sum == right_sum:
                return mid
            if abs(left_sum) > abs(right_sum):
                return binary_serach(arr, start, mid - 1)
            else:
                return binary_serach(arr, mid+1, end)

        return binary_serach(nums, start=0, end=n)

print(Solution().pivotIndex([-1,-1,-1,0,1,1]))