import numpy as np

n = int(input())
p = np.array(list(map(int, input().split())))
index = p.argsort()
ans = 0
