n,e=[int(i) for i in input().split()]
k = [int(i) for i in input().split()]
adjList = [list() for i in range(n)]
passed = [False for i in range(n)]

for _ in range(e) :
    a,b,w = [int(i) for i in input().split()]
    adjList[a].append((b,w))
    adjList[b].append((a,w))
ans = set()
def dfs(u,w):
    passed[u] = 1
    for v in adjList[u]:
        if not passed[v[0]]:
            #print(u,v[0],w+v[1])
            ans.add(w+v[1])
            dfs(v[0],w+v[1])
    passed[u] = 0
for i in range(n):
    dfs(i,0)
for e in k:
    if e in ans:
        print("YES")
    else: print("NO")
#print(adjList)


