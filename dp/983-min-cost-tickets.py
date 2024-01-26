import sys


class Solution:
    def mincostTickets(self, days, costs):
        n = len(days)
        dp = [sys.maxsize] * (n+1)
        # dp[n] = 0
        # k = n-1
        dp[0] = 0
        k = 1
        while k < n:
            day1 = costs[0] + dp[k-1]

            # day 7 pass
            seven_pass_valid = days[k] + 7
            new_index = k
            while (new_index < len(days)) and (days[new_index] < seven_pass_valid):
                new_index += 1
            day7 = costs[1] + dp[new_index]

            # day 30 pass
            thirty_pass_valid = days[k] + 30
            new_index = k
            while (new_index < len(days)) and (days[new_index] < thirty_pass_valid):
                new_index += 1
            day30 = costs[2] + dp[new_index]
            dp[k] = min(day1, day7, day30)
            k += 1
        print(dp)
        return dp[0]

class Solution1:
    def mincostTickets(self, days, costs):
        n = len(days)
        dp = [sys.maxsize] * (n+1)
        dp[n] = 0
        k = n-1
        while k >= 0:
            day1 = costs[0] + dp[k+1]

            # day 7 pass
            seven_pass_valid = days[k] + 7
            new_index = k
            while (new_index < len(days)) and (days[new_index] < seven_pass_valid):
                new_index += 1
            day7 = costs[1] + dp[new_index]

            # day 30 pass
            thirty_pass_valid = days[k] + 30
            new_index = k
            while (new_index < len(days)) and (days[new_index] < thirty_pass_valid):
                new_index += 1
            day30 = costs[2] + dp[new_index]
            dp[k] = min(day1, day7, day30)
            k -= 1
        print(dp)
        return dp[0]

# print(Solution().mincostTickets(days= [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
print(Solution().mincostTickets(days= sorted([2,5], reverse=True), costs = [1,4,25]))
print(Solution1().mincostTickets(days= [2,5], costs = [1,4,25]))
# print(Solution1().mincostTickets(days= [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
