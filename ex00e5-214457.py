def combi(n,k,idx,sol,check_k,maxK):
    maxK = max(check_k, maxK)
    if idx < n:
        combi(n,k,idx+1,sol+'0',0,maxK)
        combi(n,k,idx+1,sol+'1',check_k+1,maxK)
    else:
        if k <= maxK:
            print(sol)
    
[n,k] = [int(e) for e in input().split()]
combi(n,k,0,"",0,0)
