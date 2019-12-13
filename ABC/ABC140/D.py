n, k = map(int, input().split())
s = list(input())
c = s[0]
con = 1
odd = []
even = []
now = 1
ans = 0

for i in range(1, n):
    if s[i] == c:
        con += 1
    else:
        c = s[i]
        if not con == 1:
            ans += con - 1
        if now == 1:
            odd += [con]
            now = 2
        elif now == 2:
            even += [con]
            now = 1
        con = 1
else:
    if not con == 1:
        ans += con - 1
    if now == 1:
        odd += [con]
    elif now == 2:
        even += [con]

odd_l = len(odd)
even_l = len(even)
length = min(odd_l, even_l)
if k >= length:
    print(n-1)
else:
    print(ans + k * 2)
