import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
err = 0

for i in range(n):
    if err == 3:
        print("NO")
        sys.exit()
    if not p[i] == i+1:
        err += 1
print("YES")
