def solve(a,n,v,r):
    if len(v) == n:
        print(*r,sep='')
        return 
    for i in range(n):
        if i not in v:
            v.append(i)
            r.append(a[i])
            solve(a,n,v,r)
            r.pop()
            v.pop()
a = '123' 
r = []
v = []
n = len(a) 
solve(a,n,v,r) 
    