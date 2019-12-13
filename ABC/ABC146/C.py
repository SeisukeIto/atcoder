a, b, x = map(int, input().split())
l = 0
r = x

while not l + 1 == r:
    n = (r+l)//2
    if a*n+b*len(str(n)) > x:
        r = n
    else:
        l = n

if l > 1000000000:
    print(1000000000)
else:
    print(l)
