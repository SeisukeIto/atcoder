n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
pre = 100
ans = 0

for i in a:
    ans += b[i-1]
    if i == pre + 1:
        ans += c[i-2]
    pre = i
print(ans)
