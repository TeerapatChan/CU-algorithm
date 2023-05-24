n,a,b,c = [int(e) for e in input().split()]

dp = [0 for e in range(n+1)]
parts = [a,b,c]
parts.sort()
        
for e in parts:
    dp[e] = 1

for i in range(1,n+1):
    for e in parts:
        if i - e >= 0 and dp[i-e] > 0:
            dp[i] = max(dp[i], dp[i-e]+1)
print(dp[n])