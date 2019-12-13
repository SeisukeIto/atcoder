import math
n = int(input())
coo = []
sum = 0
con = 0
for i in range(n):
    coo.append(tuple(map(int, input().split())))

for i in range(n-1):
    for j in range(i+1, n):
        sum += math.sqrt((coo[i][0]-coo[j][0])**2+(coo[i][1]-coo[j][1])**2)
        con += 1
fact = math.factorial(n)
num = fact*(n-1)/con
print(sum*num/fact)
