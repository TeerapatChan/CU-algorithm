
n,k = [int(e) for e in input().split()]
bnm = [[0 for e in range(k+1)] for e in range(n+1)]


def binomial(n,k):
    if n == k or k == 0:
        bnm[n][k] = 1
        return 1
    if bnm[n][k] != 0: return bnm[n][k]
    for i in range(n):
        for j in range(k):
            bnm[n][k] = binomial(n-1,k-1) + binomial(n-1,k)
    return bnm[n][k]
print(binomial(n,k))