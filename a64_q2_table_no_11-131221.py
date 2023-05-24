m = int(1e8) + 7
n = int(input())
dp = [[0,0] for i in range(n+1)]
dp[2][0] = 3
dp[2][1] = 4
for i in range(3,n+1):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]%m
    dp[i][1] = dp[i-1][0]*2+dp[i-1][1]%m
print(sum(dp[n])%m)