import sys
sys.setrecursionlimit(100000)

n = int(input())
board = [int(e) for e in input().split()]
dp = [-1 for e in range(n+1)]
def billboard(idx):
    if idx >= n:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    ans = 0
    ans = max(billboard(idx+3)+board[idx], billboard(idx+1), billboard(idx+2))
    dp[idx] = ans
    return ans

print(billboard(0))
#print(dp)

