p,q,k = [int(e) for e in input().split()]

def solve(p,q):
    if q == 1:
        return p%k
    if q % 2 == 0:
        ans = solve(p,q//2)**2
        return ans%k
    else:
        ans = solve(p,q//2)**2 * (p%k)
        return ans%k
#2^5 = 2^2*2^2
    
print(solve(p,q))