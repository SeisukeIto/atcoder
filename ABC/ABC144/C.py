import math

n = int(input())
ans=n

for i in range(1, int(math.sqrt(n))+1):
    if n%i == 0:
        j = n // i
        ans = min(ans, i+j-2)
print(ans)
