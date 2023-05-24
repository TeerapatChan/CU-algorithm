n,m = [int(e) for e in input().split()]
sq = []
for i in range(n):
    x = [e for e in input().split()]
    sq.append(x)

dp = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif sq[i][0][j] == '1':
            dp[i][j] = 1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
ans = 1
for e in dp:
    ans = max(max(e),ans)
print(ans)
