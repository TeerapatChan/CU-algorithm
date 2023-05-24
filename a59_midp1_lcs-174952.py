#import numpy as np

n,m = [int(e) for e in input().split()]

x = input()
y = input()
table = []
for i in range(n+1):
    l = [int(e) for e in input().split()]
    table.append(l)
idx = []
for i in range(1,m+1):
    if table[n][i] > table[n][i-1]:
        idx.append(i-1)
ans = ''
for e in idx:
    ans = ans + y[e]
print(ans)
