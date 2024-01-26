mod = 1000000007

def countDerangements(n):
    if n <= 2:
        return n-1
    ans = (n-1 )* (countDerangements(n-2) + countDerangements(n-1))
    return ans


def countDerangementsDP(n, dp):
    if n <= 2:
        return n-1
    if dp[n] != -1:
        return dp[n]

    ans = ((n-1) * (countDerangements(n-2) + countDerangements(n-1))) % mod
    dp[n] = ans
    return dp[n]



x = 1000
dp = [-1] * (x+1)
from timeit import default_timer as timer

# start = timer()
# print(countDerangements(x))
# end = timer()
# print(end - start)

start = timer()
print(countDerangementsDP(x, dp))
end = timer()
print(end - start)


