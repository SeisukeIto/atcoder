n, m = map(int, input().split())
b = [False]*(n+2)
for _ in range(m):
    i = int(input())
    b[i] = True
M = 10**9+7
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    if b[i] == False:
        dp[i] = (dp[i-1] + dp[i-2])%M
print(dp[n])
