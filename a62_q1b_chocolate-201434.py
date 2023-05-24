import sys
sys.setrecursionlimit(10000)
n,k = [int(e) for e in input().split()]
c = set([int(e) for e in input().split()])
l = [0 for e in range(n+1)]

def chocolate(n):
    if n == 0:
        return 1
    if l[n] != 0:
        return l[n]
    ans = 0
    for piece in c:
        if n >= piece:
            ans = (ans + chocolate(n - piece) % 1000003) % 1000003
    l[n] = ans
    return ans

            
print(chocolate(n))