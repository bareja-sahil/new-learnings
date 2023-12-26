class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):

        output = len(arr1)
        sorted_arr = sorted(arr2)
        def sort_arr(arr2, num):
            nonlocal output
            end = len(arr2)
            start = 0 
            print(end)
            mid = (start + end) //2
            # print(mid)
            print(arr2[mid])
            if abs(arr2[mid] - num) <=2:
                output -= 1
            else:
                sort_arr(arr2[mid+1:], num)
        for a in arr1:
            sort_arr(sorted_arr, a)
        return output

print(Solution().findTheDistanceValue([4,5,8], [10,9,1,8], 2))