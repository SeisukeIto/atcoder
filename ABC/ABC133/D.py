n = int(input())
a = list(map(int, input().split()))
rain = [None]*(n+1)
rain[0] = 0

for i in range(n):
    rain[i+1] = a[i]*2 - rain[i]

x = rain[n] / 2

for i in range(n):
    if i % 2 == 0:
        print(int(rain[i] + x), end= " ")
    else:
        print(int(rain[i] - x), end= " ")
