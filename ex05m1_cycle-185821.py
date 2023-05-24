
def solve(G,color):
    parent = [e for e in range(len(G))]
    for i in range(len(G)):
        if color[i] == 0:
            if isCycle(G,i,color,parent):
                return True
    return False
   
def isCycle(G,u,color,parent):
    color[u] = 1
    for v in G[u]:
        if parent[u] != v:
            if color[v] == 1: return True
            if color[v] == 0:
                parent[v] = u
                if isCycle(G,v,color,parent): return True
    color[u] = 2
    return False

n = int(input())
for i in range(n):
    v,e = [int(e) for e in input().split()]
    G = [[]for x in range(v)]
    color = [0 for e in range(len(G))]
    for j in range(e):
        x,y = [int(e) for e in input().split()]
        G[x].append(y)
        G[y].append(x)
    print("YES" if solve(G,color) else "NO")

