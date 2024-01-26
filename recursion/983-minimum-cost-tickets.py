class Solution:
    def mincostTickets(self, days, costs):
        dp = [-1] * (len(days) + 1)

        def recurse(days, costs, index, dp):

            if index >= len(days):
                return 0
            if dp[index] != -1:
                return dp[index]
            # day 1 pass
            day1 = costs[0] + recurse(days, costs, index+1, dp)

            # day 7 pass
            seven_pass_valid = days[index] + 7
            new_index = index
            while (new_index < len(days)) and (days[new_index] < seven_pass_valid):
                new_index += 1
            day7 = costs[1] + recurse(days, costs, new_index, dp)

            # day 30 pass
            thirty_pass_valid = days[index] + 30
            new_index = index
            while (new_index < len(days)) and (days[new_index] < thirty_pass_valid):
                new_index += 1
            day30 = costs[2] + recurse(days, costs, new_index, dp)
            dp[index] = min(day1, day7, day30)
            return dp[index]

        return recurse(days, costs, 0, dp)


print(Solution().mincostTickets(days= [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
