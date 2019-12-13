n = int(input())
h = list(map(int, input().split()))
l = []
res = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        res += 1
    else:
        l += [res]
        res = 0
l += [res]

print(max(l))
