from math import factorial

n, k = map(int, input().split())
red = n - k
m = 10**9+7

def com_cal(p, q):
    return factorial(p) // (factorial(p - q) * factorial(q))

for i in range(1, k+1):
    if red+1 < i:
        print(0)
        continue
    com = com_cal(red + 1, i)
    div_num = com_cal(k - 1, i - 1)
    print((com * div_num)%m)
