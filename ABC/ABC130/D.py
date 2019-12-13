n, k = map(int, input().split())
a = list(map(int, input().split()))
r = 0
ans = 0
sum = a[0]

for l in range(n):
    while 1:
        if sum < k:
            r += 1
            if r >= n:
                break
            else:
                sum += a[r]
        else:
            ans += n - r
            break
    sum -= a[l]
print(ans)
