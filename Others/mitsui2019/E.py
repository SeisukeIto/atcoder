n = int(input())
a = list(map(int, input().split()))
m = 10**9+7
lst = [0]*n
zeros = 0
ans = 3

for num in a:
    lst[num] += 1
    if not num == 0:
        ans*=lst[num-1]
    else:
        zeros += 1
        if zeros == 2:
            ans *= 2
    ans%=m
print(ans%m)
