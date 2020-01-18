n = int(input())
dic = {}

for i in range(n):
    inp = list(map(int, input().split()))
    dic[inp[0]] = inp[1]

dic = sorted(dic.items())
ans = 1
pre = dic[0][0]+dic[0][1]
fidx = 0
for i in range(1, n):
    n_s = dic[i][0]+dic[i][1]
    if pre > n_s:
        pre = n_s
        fidx = i
idx = fidx

for i in range(fidx+1, n):
    if dic[idx][0]+dic[idx][1] > dic[i][0]-dic[i][1]:
        if dic[idx][0]+dic[idx][1] > dic[i][0]+dic[i][1]:
            idx = i
    else:
        ans += 1
        idx = i


print(ans)
