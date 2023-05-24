import sys

n,p  = [int(i) for i in sys.stdin.readline().split()]
p=2**p

def isVirus(ls,start,stop):
    if (stop-start) <= 2: return True
    mid = (start+stop)//2
    if(abs(ls.count("1",start ,mid ) - ls.count("1",mid ,stop)) > 1 ) :
        return False
    return isVirus(ls,start,mid) and isVirus(ls,mid,stop)

for i in range(n):
    l =  sys.stdin.readline()[:-1].replace(" ", "")
    print("yes" if isVirus(l,0,p) else "no")

# 1 0 0 0 // 1 1 1 1
