n,m = [int(e) for e in input().split()]
used = [0 for i in range(n)]
d = dict()
for i in range(m):
    x,y = [int(e) for e in input().split()]
    d[y] = x

def permu_before(idx,s):
    if idx < n:
        for i in range(n):
            if used[i] == 0 and (i not in d or used[d[i]] == 1):
                used[i] = 1
                permu_before(idx+1,s+str(i)+" ")
                used[i] = 0
    else:
        print(s.strip())
    
permu_before(0,'')
