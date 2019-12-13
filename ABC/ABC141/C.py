n, k, q = map(int, input().split())
cor = [0]*n

for i in range(q):
    cor[int(input()) - 1] += 1

for i in range(n):
    if k - q + cor[i] > 0:
        print("Yes")
    else:
        print("No")
