import math
n, d = map(int, input().split())
x = [None]*n
ans = 0

for i in range(n):
    x[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        res = 0
        for k in range(d):
            res += (x[i][k] - x[j][k])**2
        res = math.sqrt(res)
        if res.is_integer():
            ans += 1
print(ans)
