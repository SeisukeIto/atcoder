n, k, s = map(int, input().split())

for i in range(n):
    if i < k:
        print(s, end=" ")
    else:
        if s == 10**9:
            print(1, end=" ")
        else:
            print(s+1, end=" ")
