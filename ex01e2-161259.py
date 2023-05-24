import sys
sys.setrecursionlimit(1000000)
n = int(input())
l = [int(e) for e in input().split()]
dp = [ -99999 for i in range(n+1)]
def mss(idx):
    if idx == 0:
        return l[0]
    if dp[idx] != -99999:
        return dp[idx]
    ans = max(l[idx], mss(idx-1) + l[idx])
    dp[idx] = ans
    return ans
mss(n-1)
print(max(dp))