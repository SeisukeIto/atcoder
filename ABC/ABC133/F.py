n, q = map(int, input().split())
edges = [None]*(n-1)
qst = [None]*q

for i in range(n-1):
    edges[i] = list(map(int, input().split()))

for i in range(q):
    qst[i] = tuple(map(int, input().split()))

for i in range(q):
    
