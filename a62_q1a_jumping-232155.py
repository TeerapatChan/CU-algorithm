import sys 
sys.setrecursionlimit(10000000)

n = int(input())
x = [int(e) for e in input().split()]
jumped = dict()
def jump(idx):
    if idx >= n:
        return 0
    
    
    if idx in jumped:
        return jumped[idx]
        
    b = max(jump(idx+1),jump(idx+2),jump(idx+3)) + x[idx]
    jumped[idx] = b
    return b
ans = jump(0)


if x[-1] < 0 and (x[-2] >= 0 or x[-3] >= 0):
    ans += x[-1]

print(ans)