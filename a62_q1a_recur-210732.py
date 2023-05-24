a,b = [int(e) for e in input().split()]
l=[[0 for i in range(2**a)] for x in range(2**a)]
def solve(n,a,b,row,column):
    if n == 0:
        l[row][column] = str(b)
        return
    n = n // 2
    solve(n,a-1,b,row,column)
    solve(n,a-1,b-1,row,column+n)
    solve(n,a-1,b+1,row+n,column)
    solve(n,a-1,b,row+n,column+n)
    
solve(2**a,a,b,0,0)
for r in l:print(" ".join(r))


