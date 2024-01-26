import sys


class Solution:
    def mincostTickets(self, days, costs):
        ans = 0
        weekly_queue = []
        monthly_queue = []
        for day in days:
            if len(weekly_queue) > 0 and weekly_queue[0][0] <= (day+7):
                weekly_queue.pop()
            if len(monthly_queue) > 0 and monthly_queue[0][0] <= (day+30):
                monthly_queue.pop()
            weekly_queue.append((day, ans+costs[1]))
            monthly_queue.append((day, ans+costs[2]))







print(Solution().mincostTickets(days= [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
