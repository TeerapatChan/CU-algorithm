import sys
kb = sys.stdin
n = int(input())
AdjList = [[] for e in range(n)]
w = [-1 for e in range(n)]
ans = []
for i in range(n):
    x,y = map(int, kb.readline().split())
    AdjList[x].append(y)
    AdjList[y].append(x)
    
def dfs(Adj,u,p):
    for v in Adj[u]:
        if p != v:
            if w[v] != -1:
                return w[u]-w[v]+1
            w[v] = w[u]+1
            x = dfs(Adj,v,u)
            if x > 0: return x
    return -1

print(dfs(AdjList,0,-1))
#print(ans)