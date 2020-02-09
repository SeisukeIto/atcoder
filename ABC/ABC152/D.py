n = int(input())
grid = [[0 for i in range(9)] for j in range(9)]
ans = 0

for i in range(1, n+1):
    s = str(i)
    if int(s[0]) == 0 or int(s[-1]) == 0:
        continue
    grid[int(s[0])-1][int(s[-1])-1] += 1

for i in range(9):
    for j in range(i, 9):
        if i == j:
            ans += grid[i][j] * grid[j][i]
        else:
            ans += (grid[i][j] * grid[j][i])*2

print(ans)
