from collections import defaultdict
import bisect
s = input()
t = input()
ls = len(s)
dbls = s*2
idx = 0
ans = 0
dic = defaultdict(list)

for i, c in enumerate(dbls):
    dic[c] += [i+1]

for c in t:
    if not c in dic.keys():
        print(-1)
        exit()
    lst = dic[c]
    i = bisect.bisect_right(lst, idx)
    idx = lst[i]
    if idx > ls:
        ans += ls
        idx -= ls
    else:
        idx = lst[i]

if not idx == 0:
    ans += idx
print(ans)
