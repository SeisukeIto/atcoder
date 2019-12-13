m, d = map(int, input().split())
ans = 0

for i in range(22, d+1):
    num = str(i)
    d_1 = int(num[-1])
    d_10 = int(num[-2])
    if 0 < d_1 * d_10 <= m and d_1 > 1 and d_10 > 1:
        ans += 1
print(ans)
