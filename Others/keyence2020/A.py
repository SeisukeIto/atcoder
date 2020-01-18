h = int(input())
w = int(input())
n = int(input())

if h > w:
    x = h
else:
    x = w

if n%x == 0:
    print(int(n//x))
else:
    print(int(n//x)+1)
