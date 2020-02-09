n, k = map(int, input().split())
p = list(map(int, input().split()))
lst = [0]*(n+1)
lst[1] = (p[0]+1)/2

for i in range(2, n+1):
    lst[i] = lst[i-1] + (p[i-1]+1)/2

max = 0

for i in range(n-k+1):
    if max < lst[i+k]-lst[i]:
        max = lst[i+k]-lst[i]

print(max)
