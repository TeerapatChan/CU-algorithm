def mul(x,l,k):
    return [(x[0]*l[0]+x[1]*l[2])%k,
    (x[0]*l[1]+x[1]*l[3])%k,
    (x[2]*l[0]+x[3]*l[2])%k,
    (x[2]*l[1]+x[3]*l[3])%k]

def solve(l,n,k):
    if n == 1: return mul(l,[1,0,0,1],k)
    if n % 2 == 0:
        m = solve(l,n//2,k)
        return mul(m,m,k)
    else:
        m = solve(l,n//2,k)
        x = mul(m,m,k)
        return mul(x,l,k)
n,k = [int(e) for e in input().split()]
l = [int(e) for e in input().split()]
for e in solve(l,n,k):
    print(e,end=' ')
