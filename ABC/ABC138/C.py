n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
sum = lst[0]

for i in range(1, n):
    sum = (sum + lst[i]) / 2
print(sum)
