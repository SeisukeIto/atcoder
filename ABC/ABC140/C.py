n = int(input())
b = list(map(int, input().split()))
a = [None]*n
a[0] = b[0]
ans = a[0]

for i in range(n-2):
    a[i+1] = min(b[i], b[i+1])
    ans += a[i+1]
ans += b[n-2]
print(ans)
