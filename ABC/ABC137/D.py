from collections import deque
import heapq
n, m = map(int, input().split())
jobs = [None]*n
q = []
heapq.heapify(q)
day = 0
ans = 0

for i in range(n):
    jobs[i] = tuple(map(int, input().split()))
jobs.sort(key = lambda x:x[1], reverse=True)
jobs.sort(key = lambda x:x[0])
jobs = deque(jobs)

for i in range(m):
    while True:
        if  not len(jobs) == 0:
            j = jobs.popleft()
            if not j[0] == i+1:
                jobs.appendleft(j)
                break
            else:
                heapq.heappush(q, -j[1])
        else:
            break
    if q:
        ans -= heapq.heappop(q)
print(ans)
