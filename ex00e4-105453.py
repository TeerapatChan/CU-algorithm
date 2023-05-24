def combi(a,b,idx,check,sol):
    if(idx != b):
        combi(a,b,idx+1,check,sol+'0')
        combi(a,b,idx+1,check+1,sol+'1')
    elif check == a: print(sol)
[a,b] = [int(e) for e in input().split()]
combi(a,b,0,0,'')
