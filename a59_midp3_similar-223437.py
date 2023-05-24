def s(a,b):
    if len(a) == 1:
        if a==b: return True
        else: return False
    mid1 = len(a)//2
    mid2 = len(b)//2
    return (s(a[:mid1],b[:mid2]) and s(a[mid1:],b[mid2:])) or (s(a[:mid1],b[mid2:]) and s(a[:mid1],b[mid2:]))
    
s1 = input()
s2 = input()
if s(s1,s2):print('YES')
else: print('NO')