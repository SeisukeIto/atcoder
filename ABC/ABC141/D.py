import heapq
n ,m = map(int, input().split())
a = list(map(lambda x:int(x)*(-1), input().split()))
heapq.heapify(a)
ans = 0

for i in range(m):
    x = heapq.heappop(a)
    heapq.heappush(a, x/2)

for i in range(n):
    ans -= int(a[i])
print(ans)
