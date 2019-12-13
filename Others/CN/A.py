n, b_1, b_2, b_3 = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
r = [list(map(int, input().split())) for _ in range(n)]
grid = [[None]*n for _ in range(n)]
w_dp = [[None]*n for _ in range(n)]
h_dp = [[None]*n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if i == 0 and j == 0:
            grid[i][j] = r[i][j]
            w_dp[i][j] = grid[i][j]
            h_dp[i][j] = grid[i][j]
        else:
            if w_dp[i][j-1] + r[i][j] <= b_1:
                grid[i][j] = r[i][j]
            elif w_dp[i][j-1] + l[i][j] <= b_1:
                grid[i][j] = b_1 - w_dp[i][j-1]
            else:
                grid[i][j] = r[i][j]
            w_dp[i][j] = w_dp[i][j-1] + grid[i][j]
