import sys
sys.setrecursionlimit(100000)
kb = sys.stdin
n,m,k = [int(e) for e in kb.readline().split()]
b = [int(e) for e in kb.readline().split()]
fire = [int(e) for e in kb.readline().split()]
adjList = [[] for e in range(n)]
for i in range(m):
    x,y = [int(e) for e in input().split()]
    adjList[x].append(y)
    
def dfs(adjList,u):
    #print(u)
    b[u] = 0
    for v in adjList[u]:
        if b[v]:
            dfs(adjList,v)
ans = []
for i in range(k):
    dfs(adjList,fire[i])
    ans.append(sum(b))
for e in ans:
    print(e,end=" ")

