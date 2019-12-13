import sys
input = sys.stdin.readline

n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
ans = 0

for i in range(n):
    b = b_lst[-(i+1)]
    a = a_lst[-(i+1)]
    pre_a = a_lst[-(i+2)]
    if a >= b:
        ans += b
    else:
        if b - a > pre_a:
            a_lst[-(i+2)] = 0
            ans += a + pre_a
        else:
            a_lst[-(i+2)] -= b - a
            ans += b
print(ans)
