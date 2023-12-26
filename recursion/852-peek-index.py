class Solution:
    def peakIndexInMountainArray(self, arr):
        n = len(arr) - 1

        def binary_serach(arr, start, end):
            mid = (start + end) // 2
            if mid > 0 and (mid + 1) <= n:
                if arr[mid-1] < arr[mid] > arr[mid+1]:
                    return mid
            if mid > 0 and arr[mid-1] < arr[mid]:
                return binary_serach(arr, mid+1, end)
            else:
                return binary_serach(arr, start, mid)
        return binary_serach(arr, start=0, end=n)

print(Solution().peakIndexInMountainArray([0,1,2,0]))