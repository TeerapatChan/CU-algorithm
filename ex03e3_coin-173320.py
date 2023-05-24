import sys 
sys.setrecursionlimit(10000000)

n, v = [int(e) for e in input().split()]
c = [int(e) for e in input().split()]
ans = 0
dp = [-1 for e in range(v+1)]

def f(value):
    if value == 0:
        return 0
    if dp[value] != -1:
        return dp[value]
    sub = 0
    ans = float('inf')
    for i in range(n):
        if value - c[i] >= 0:
            sub = f(value - c[i])
            ans = min(sub + 1, ans)
    dp[value] = ans
    return dp[value]

print(f(v))
    
#print(dp)

