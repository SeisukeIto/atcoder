n = int(input())
w = list(map(int, input().split()))
sum = 0
sum_2 = 0

for i in range(n):
    sum += w[i]
half = sum/2

for i in range(n):
    sum_2 += w[i]
    if sum_2 >= half:
        ans = min(sum_2-half, half-ans)
        break
    else:
        ans = sum_2
print(int(ans*2))
