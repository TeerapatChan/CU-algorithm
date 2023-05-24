import sys
sys.setrecursionlimit(100000)
def mss(idx,l):
    if idx == 0:
        return l[0]
    if mss_dp[idx] != -99999:
        return dp[idx]
    ans = max(l[idx], mss(idx-1,l) + l[idx])
    mss_dp[idx] = ans
    return ans
n = int(input())
table = []
for i in range(n):
    x = [int(e) for e in input().split()]
    table.append(x)
l = [ [] for e in range(n*2-1)]
for i in range(n):
    for j in range(n):
        if i+j < n:
            l[i].append(table[j][i+j])
for i in range(1,n):
    for j in range(n):
        if i+j < n:
            l[i+n-1].append(table[i+j][j])
      #1 0 -> 2 1 -> 3 2
ans = []
for i in range(len(l)):
    mss_dp = [-99999 for i in range(n+1)]
    mss(len(l[i])-1,l[i])
    ans.append(max(mss_dp))
print(max(ans))
#print(np.array(table))

