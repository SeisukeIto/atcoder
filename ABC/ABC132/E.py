from collections import deque
import copy, sys

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())
con = [None]*(n+1)
q = deque([s])
pre_q = deque()
dejab = []
depth = 0

for i in range(m):
    a, b = edges[i][0], edges[i][1]
    if con[a] == None:
        con[a] = [b]
    else:
        con[a] += [b]

count = 1
while not len(q) == 0:
    depth += 1
    pre_q = copy.copy(q)
    if list(q) in dejab and count == 1:
        print(-1)
        sys.exit()
    elif count == 1:
        dejab.append(list(q))
    q.clear()
    for p in pre_q:
        if con[p] == None:
            continue
        for c in con[p]:
            if c == t and count == 3:
                print(int(depth / 3))
                sys.exit()
            q.append(c)
    if count < 3:
        count += 1
    else:
        count = 1
print(-1)
