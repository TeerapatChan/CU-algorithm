n,m =[int(e) for e in input().split()]
forest = []

for i in range(n):
    x = [int(e) for e in input().split()]
    forest.append(x)
    
dp = [[0 for e in range(m)] for e in range(n)]

dp[0][0] = forest[0][0]
for i in range(1,m):
    dp[0][i] = dp[0][i-1]+forest[0][i]
for i in range(1,n):
    dp[i][0] = dp[i-1][0]+forest[i][0]

for i in range(1,n):
    for j in range(1,m):
        #print(forest[i][j])
        point = forest[i][j]
        dp[i][j] = max(dp[i-1][j-1]+point*2,dp[i-1][j]+point, dp[i][j-1]+point)
print(dp[n-1][m-1])
        

