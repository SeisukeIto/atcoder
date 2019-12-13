import math
n = int(input())

x = n // 1.08

if math.floor((x+1)*1.08) == n:
    print(int(x+1))
else:
    print(":(")
