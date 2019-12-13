A, B = map(int, input().split())
sum = A + B
dif = A - B
pro = A * B

max = sum
if dif > max:
    max = dif
if pro > max:
    max = pro

print(max)
