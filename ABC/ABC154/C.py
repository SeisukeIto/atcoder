from collections import defaultdict
dic = defaultdict(int)
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    dic[a[i]] += 1
    if dic[a[i]] == 2:
        print("NO")
        break
else:
    print("YES")
