h, w = map(int, input().split())
grid = [None]*h
cnt = [[0 for _ in range(w+1)] for __ in range(h+1)]
for i in range(h):
    grid[i] = list(input())
for i in range(h):
    done = [0]*w
    for j in range(w):
        if grid[i][j] == "#": continue
        if done[j] == 1: continue
        l = 0
        while j+l < w:
            if grid[i][j+l] == "#": break
            l += 1
        for k in range(l):
            cnt[i][j+k] += l
            done[j+k] = 1
for j in range(w):
    done = [0]*h
    for i in range(h):
        if grid[i][j] == "#": continue
        if done[i] == 1: continue
        l = 0
        while i+l < h:
            if grid[i+l][j] == "#": break
            l += 1
        for k in range(l):
            cnt[i+k][j] += l
            done[i+k] = 1
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, cnt[i][j]-1)
print(ans)
