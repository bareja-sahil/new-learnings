import sys


class Solution:
    def distributeCookies(self, cookies, k):

        idx = 0
        ans = sys.maxsize
        n = len(cookies)
        bucket = [0] * k

        def distribute(idx):
            nonlocal ans
            print(bucket)
            if idx == n:
                return max(bucket)
            for i in range(k):
                print(f"{i}: {bucket}")
                bucket[i] += cookies[idx]
                ans = min(ans, distribute(idx+1))
                bucket[i] -= cookies[idx]
            return ans
        cookies.sort(reverse=True)
        distribute(0)


Solution().distributeCookies(cookies=[3, 4, 2], k=2)