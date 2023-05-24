def virus(x):
    if len(x) == 2:
        return x == ['0','1']
    mid = len(x)//2
    f = x[:mid]
    b = x[mid:]
    return virus(b) and (virus(f) or virus(f[::-1]))
    
    
m,n = [int(e) for e in input().split()]
for i in range(m):
    x = input().split()
    if virus(x):
        print('yes')
    else: print('no')
