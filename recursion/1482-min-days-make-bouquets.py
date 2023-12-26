class Solution:
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1

        def is_possible(bloomday, mid, m, k):
            flowers = 0
            boquets = 0
            for i in bloomday:
                if i <= mid:
                    flowers += 1
                else:
                    flowers = 0
                if flowers == k:
                    boquets += 1
                    flowers = 0
            return boquets >= m


        start = 1
        end = max(bloomDay)
        while start < end:
            mid = (start + end ) // 2
            if is_possible(bloomDay, mid, m, k):
                end = mid
            else:
                start = mid + 1
        return end




print(Solution().minDays([1,10,2,9,3,8,4,7,5,6], m=4, k=2))