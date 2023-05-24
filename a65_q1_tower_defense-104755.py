n,m,k,w = [int(e) for e in input().split()]
mons = [int(e) for e in input().split()]
hps = [int(e) for e in input().split()]
towers = [int(e) for e in input().split()]
attacked = set()
ans = 0

for i in range(m):
    start = max(0,mons[i] - w)
    stop = min(n,mons[i]+w)
    for idx in range(start,stop+1):
        #print(mons[i],idx)
        #if idx in towers:
        #    print(idx)
        if idx in towers and (idx not in attacked):
            hps[i] -= 1
            #print(idx)
            attacked.add(idx)
        if hps[i] == 0:
            break
print(sum(hps))
    #print(attacked)
#-tmtmt-----
