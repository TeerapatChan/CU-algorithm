import bisect,sys
n,k,m = [int(e) for e in input().split()]
food = [int(e) for e in input().split()]
qsum = [0 for i in range(n+1)]
qsum[1] = food[1]-m
for i in range(1,n+1):
    qsum[i] = qsum[i-1]+food[i-1]-m
for i in range(k):
    start, use = [int(e) for e in sys.stdin.readline().split()]
    print(bisect.bisect_left(qsum, qsum[start-1]+use))