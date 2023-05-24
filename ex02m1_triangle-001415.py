import sys

n = int(input())
arr = []
for i in range(n):
    x = [int(e) for e in input().split()]
    arr.append(x)
t = [[-1 for i in range(e)] for e in range(1,n+1)]
def triangle(level, i):
    global n
    if level == n-1:
        return arr[level][i]
    
    if t[level][i] != -1:
        return t[level][i]
    
    ans = max(triangle(level+1, i), triangle(level+1, i+1)) + arr[level][i]
    t[level][i] = ans
    return t[level][i]
print(triangle(0,0))
