import sys

v,e = [int(x) for x in sys.stdin.readline().split()]

AdjList = [[] for i in range(v)]

for i in range(e):
    x,y = [int(e) for e in sys.stdin.readline().split()]
    AdjList[x].append(y)
    AdjList[y].append(x)

visited = [0 for e in range(v)]
colored = [-1 for e in range(v)]
used = set()

def checkColor(u):
    color = set()
    for v in AdjList[u]:
        if colored[v] != -1:
            color.add(colored[v])
    return color

def dfs(u):
    visited[u] = 1
    if u == 0:
        colored[u] = 0
        used.add(0)
    else:
        cannot_color = checkColor(u)
        for e in range(len(used)):
            if e not in cannot_color:
                colored[u] = e
                break
        if colored[u] == -1:
            colored[u] = len(used)
            used.add(len(used))
        
    for v in AdjList[u]:
        if not visited[v]:
            dfs(v)

dfs(0)
for i in range(v):
    if colored[i] == -1:
        dfs(i)

print(len(used))