import bisect
p,k,A,B = [int(e) for e in input().split()]
avengers = [int(e) for e in input().split()]
avengers.sort()
d = dict()
for e in avengers:
    if e not in d:
        d[e] = 1
    else: d[e] += 1
def thanos(left,right):
    #print(left,right)
    if right - left == 0:
        if right in d:
            #print('avenger in',left,'-',left,'power =',B*avengers.count(right)*1)
            return B*d[right]*1
        else:
            #print('avenger not in',left,'-',left,'power =',A)
            return A
    l = right - left
    Left = thanos(left,left+l//2)
    Right = thanos(left+l//2+1,right)
    s = bisect.bisect_right(avengers,right) - bisect.bisect_left(avengers,left)
    if s == 0:
        ans = A
    else:
        ans = B*s*(right-left+1)
    return min(Left+Right, ans)

#1 1 //1 1 // 1 1// 1 1
print(thanos(1,2**p))