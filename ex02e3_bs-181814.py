n,m = [int(e) for e in input().split()]
x = [int(e) for e in input().split()]
q = [int(e) for e in input().split()]
#10 13 14 14 14 15 16 16 18 200

def BinarySearch(left,right,search):
    mid = (left+right)//2
    if left <= right:
        if x[mid] == search:
            return mid if mid+1 >= len(x) else BinarySearch(mid+1,right,search)
        elif x[mid] < search:
            return BinarySearch(mid+1,right,search)
        else:
            return BinarySearch(left,mid-1,search)
    elif x[mid] <= search: return mid
    else:
        return -1
for i in range(m):
    print(BinarySearch(0,n-1,q[i]))
