n, l = map(int, input().split())
min = abs(l)
ans = l

for i in range(2, n+1):
    pi = l + i - 1
    if abs(pi) < abs(min):
        min = pi
    ans += pi
print(ans-min)
