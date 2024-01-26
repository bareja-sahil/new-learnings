mod = 1000000007
def countDerangementsDP(n, dp):
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n+1):
        print(i)
        dp[i] = ((i-1) * (dp[i-2] + dp[i-1])) % mod
    return dp[n]


x = 1000
dp = [-1] * (x+1)
from timeit import default_timer as timer


start = timer()
print(countDerangementsDP(x, dp))
end = timer()
print(end - start)