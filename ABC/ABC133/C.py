import sys
l, r = map(int, input().split())
m = 2019
min = 2019

if r - l >= 2019:
    print(0)
else:
    l, r = l%m, r%m
    for i in range(l, r):
        for j in range(i+1, r+1):
            if min > (i * j)%m:
                min = (i * j)%m
    print(min)
