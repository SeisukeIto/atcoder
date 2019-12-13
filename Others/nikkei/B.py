import sys
M = 998244353

n = int(input())
d = list(map(int, input().split()))
idx = [0]*n
ans = 1
for i in range(n):
    idx[d[i]] += 1

if not d[0] == 0 or not idx[0] == 1:
    print(0)
else:
    for i in range(1,n):
        if idx[i-1] == 0:
            if not idx[i] == 0:
                print(0)
                sys.exit()
        else:
            ans *= idx[i-1]**idx[i]%M
    else:
        print(ans%M)
