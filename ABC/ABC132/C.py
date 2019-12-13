import sys

n = int(input())
d = list(map(int, input().split()))
dic = {}
val = 0

for i in range(n):
    if d[i] in dic.keys():
        dic[d[i]] += 1
    else:
        dic[d[i]] = 1

dic = sorted(dic.items())

if len(dic) == 1:
    print(0)
    sys.exit() 

for i in range(len(dic) - 1):
    val += dic[i][1]
    if val == n//2:
        ans = (dic[i][0], dic[i+1][0])
        print(ans[1] - ans[0])
        break
    elif val > n//2:
        print(0)
        break
