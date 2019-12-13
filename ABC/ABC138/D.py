from collections import deque
n, Q = map(int, input().split())
edges = [[] for _ in range(n+1)]
count = [0]*(n+1)
q = deque()
q.append((1, 0))

for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for _ in range(Q):
    p, x = map(int, input().split())
    count[p] += x

while(q):
    k = q.popleft()
    count[k[0]] += count[k[1]]
    for i in edges[k[0]]:
        if not i == k[1]:
            q.append((i, k[0]))

print(*count[1:])
