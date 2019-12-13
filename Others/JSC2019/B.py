n, k = map(int, input().split())
a = list(map(int, input().split()))
m = 10**9+7
p, q = 0, 0

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            if i < j: p += 1
            q += 1

print((p*k + (q*k*(k-1) // 2)) % m)
