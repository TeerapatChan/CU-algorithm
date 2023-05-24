import sys,copy
kb = sys.stdin
def isValid(grid,r,c):
    if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
        return False
    return True

r,c,T = [int(e) for e in kb.readline().split()]
grid = []
for i in range(r):
    x = [int(e) for e in kb.readline().split()]
    grid.append(x)
for t in range(T):
    g = [[i for i in row] for row in grid]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                if isValid(grid,i-1,j) and grid[i-1][j] == 0:
                    g[i-1][j] = 1
                if isValid(grid,i+1,j) and grid[i+1][j] == 0:
                    g[i+1][j] = 1
                if isValid(grid,i,j-1) and grid[i][j-1] == 0:
                    g[i][j-1] = 1
                if isValid(grid,i,j+1) and grid[i][j+1] == 0:
                    g[i][j+1] = 1
                #print(grid[i][j],np.array(grid))
    grid = [[i for i in row] for row in g]
s = 0
for l in grid:
    for e in l:
        if e == 1:
            s += 1
print(s)
            
