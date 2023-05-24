n,e,k = [int(e) for e in input().split()]
AdjList = [[] for e in range(n+1)]
visited = [False for e in range(n+1)]
dist = [0 for e in range(n+1)]
for i in range(e):
    x,y = [int(e) for e in input().split()]
    AdjList[x].append(y)
    AdjList[y].append(x)

def bfs(AdjList,s):
    d = [0 for e in range(len(AdjList))]
    queue = [s]
    while(queue):
        u = queue.pop(0)
        for v in AdjList[u]:
            if d[v] == 0 and v != 0:
                d[v] = d[u]+1
                queue.append(v)
    return d

d = bfs(AdjList,0)
print(0 if sum(d) == 0 else d.count(k))
    

