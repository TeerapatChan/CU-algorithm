import sys,heapq
kb = sys.stdin
n = int(input())
AdjMat = []
for i in range(n):
    x = [int(e) for e in kb.readline().split()]
    AdjMat.append(x)
queue = [(0,0)]
heapq.heapify(queue)
d = [float('inf') for e in range(n)]
d[0] = 0
while(queue):
    front = heapq.heappop(queue)
    u = front[1]
    for i in range(len(AdjMat[u])):
        if AdjMat[u][i] > 0 and AdjMat[u][i]+d[u] < d[i]:
            d[i] = AdjMat[u][i]+d[u]
            heapq.heappush(queue,(d[i],i))
        
#print(parent)
print(-1 if max(d) == float('inf') else max(d))
