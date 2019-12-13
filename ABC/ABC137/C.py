n = int(input())
dict = {}
ans = 0

for i in range(n):
    s = tuple(sorted(input()))
    if s in dict.keys():
        ans += dict[s]
        dict[s] += 1
    else:
        dict[s] = 1
print(ans)
