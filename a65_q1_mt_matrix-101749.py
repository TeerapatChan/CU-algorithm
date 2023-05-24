def mt(n,col,row,isNegative,mat):
    if n == 1: return mat[row-1][col-1]*isNegative
    mid = 2**n // 2
    
    if row <= mid and col <= mid:
        return mt(n-1,col,row,isNegative,mat)
    
    elif row <= mid and col > mid:
        return mt(n-1,row,col - mid,isNegative,mat)
    
    elif row > mid and col <= mid:
        return mt(n-1,col, row - mid, -1*isNegative, mat)
    
    else:
        return mt(n-1,row - mid,col - mid,-1*isNegative, mat)
    
n,m = [int(e) for e in input().split()]
u,v,w,p = [int(e) for e in input().split()]
mat = [[u,v],[w,p]]

for i in range(m):
    row,col = [int(e) for e in input().split()]
    print(mt(n,col,row,1,mat))
