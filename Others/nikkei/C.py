import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sorteda = sorted(a)
sortedb = sorted(b)
for i in range(n):
    if a[i] < b[i]:
        print(-1)
        sys.exit()
