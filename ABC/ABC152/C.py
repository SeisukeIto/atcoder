n = int(input())
p = list(map(int, input().split()))

now = p[0]
ans = 1

for i in range(1, n):
    if p[i] <= now:
        ans += 1
        now = p[i]

print(ans)
