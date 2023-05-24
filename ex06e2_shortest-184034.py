n,m,s = [int(e) for e in input().split()]
adjList = [[] for e in range(n)]
for i in range(m):
    x = [int(e) for e in input().split()]
    adjList[x[0]].append((x[1],x[2]))

def bellman(AdjList,u):
    d = [float('inf')  for e in range(len(AdjList))]
    d[u] = 0
    for k in range(1,len(AdjList)-1):
        flag = False
        for u in range(len(AdjList)):
            for j in range(len(AdjList[u])):
                v = AdjList[u][j]
                dist = v[1]
                node = v[0]
                d[node] = min(d[node],d[u]+dist)
                flag = True
        if not flag: break
    for u in range(len(AdjList)):
        for j in range(len(AdjList[u])):
            v = AdjList[u][j]
            dist = v[1]
            node = v[0]
            if d[u]+dist < d[node]:
                return [-1]
            
    return d

b = bellman(adjList,s)
print(" ".join([str(e) for e in b]))
