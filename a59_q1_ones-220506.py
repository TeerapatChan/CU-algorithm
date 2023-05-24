q = [0,1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111]

def find(n):
    for i in range(len(q)):
        if n < q[i]: return i-1;
        
def solve(n):
    if n <= 11:
        if n < 7: return n
        else: return 13-n
    else:
        length = find(n)
        times = n // q[length]
        ans = times * length + solve(n - times * q[length])
        if q[length+1]-n < n :
            ans = min(ans, length+1+solve(q[length+1]-n))
        return ans


n = int(input())
n = abs(n)
print(solve(n))