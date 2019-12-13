x = int(input())
sum = 0

n = x // 100
m = x - n*100

for i in reversed(range(1, 6)):
    sum += m // i
    m = m % i

if sum <= n:
    print(1)
else:
    print(0)
