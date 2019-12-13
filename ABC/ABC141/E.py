import sys
input = sys.stdin.readline
n = int(input())
s = input()
dp = [[0]*(n+1) for y in range(n+1)]
ans = 0
for i in range(n):
    a = n-1-i
    for j in range(n):
        b = n-1-j
        if s[a] == s[b]:dp[a][b] = dp[a+1][b+1] + 1
for i in range(n):
    for j in range(n):
        now = min(dp[i][j], j-i)
        ans = max(ans, now)
print(ans)
