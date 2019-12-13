n = int(input())
s = int(input())
lst = []

for i in range(n):
     lst.append(s%10)
     s //= 10
lst.reverse()

ten = [-1]*10
hun = [-1]*100
tho = [-1]*1000

for i in range(len(lst)):
    l = lst[i]
    for j in range(100):
        if not hun[j] == -1:
            idx = j*10 + l
            tho[idx] = 1
    for j in range(10):
        if not ten[j] == -1:
            idx = j*10 + l
            hun[idx] = 1
    ten[l] = 1

ans = 0
for i in range(1000):
    if tho[i] == 1:
        ans += 1
print(ans)
