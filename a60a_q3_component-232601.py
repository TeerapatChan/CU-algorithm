nv,ne = [int(e) for e in input().split()]
AdjList = [[] for e in range(nv+1)]
for i in range(1,ne+1):
    x,y = [int(e) for e in input().split()]
    AdjList[x].append(y)
    AdjList[y].append(x)
visited = [False for e in range(nv+1)]

def dfs(AdjList,visited,u):
    visited[u] = True
    
    for v in AdjList[u]:
        if not visited[v]:
            dfs(AdjList,visited,v)
            
def count(AdjList,visited):
    n = 0
    for v in range(1,len(AdjList)):
        if not visited[v]:
            dfs(AdjList,visited,v)
            n+=1
    return n
print(count(AdjList,visited))
