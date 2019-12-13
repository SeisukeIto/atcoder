from collections import deque
import sys
n = int(input())
q = [None]*n
for i in range(n):
    q[i] = tuple(map(int, input().split()))
q = sorted(q, key = lambda x: x[1])
q = deque(reversed(q))
job = q.popleft()
day = job[1] - job[0]
if n == 1:
    if day >= 0:
        print("Yes")
    else:
        print("No")
    sys.exit()

while q:
    job = q.popleft()
    if job[1] < day:
        day = job[1] - job[0]
    else:
        day -= job[0]
    if day < 0:
        print("No")
        break
else:
    print("Yes")
