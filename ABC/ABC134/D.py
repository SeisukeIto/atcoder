import sys
input = sys.stdin.readline

n = int(input())
a_lst = list(map(int, input().split()))
b_lst = [0]*n

def multiple_i(i, n):
        lst = []
        j = 2
        while(1):
            if i*j <= n:
                lst += [i*j]
                j += 1
            else:
                break
        return lst

for i in range(1, n+1):
    r = a_lst[-i]
    if not n+1-i > n / 2:
        mul_lst = multiple_i(n+1-i, n)
        ball = 0
        for mul in mul_lst:
            if b_lst[mul - 1] == 1:
                ball += 1
        if not ball % 2 == r:
            b_lst[-i] = 1
    else:
        if r == 1:
            b_lst[-i] = 1

m = 0
ans_lst = []
for i in range(n):
    if b_lst[i] == 1:
        m += 1
        ans_lst += [i + 1]

print(m)
for i in range(m):
    print(ans_lst[i], end=" ")
