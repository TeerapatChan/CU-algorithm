def bns(x,y,l,h):
    mid = (l+h)//2
    if mid >= len(x): return x[-1]
    if h >= l:
        if y == x[mid]:
            return x[mid]
        elif y > x[mid]:
            return bns(x,y,mid+1,h)
        else:
            return bns(x,y,l,mid-1)
    elif x[mid] <= y: return x[mid]    
    else: return -1
n,m = [int(e) for e in input().split()]
l = [int(e) for e in input().split()]
q = [int(e) for e in input().split()]
for i in range(m):
    print(bns(l,q[i],0,n))
