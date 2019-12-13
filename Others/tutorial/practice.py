import sys

N = int(input())
t = [0]
x = [0]
y = [0]

for i in range(1, N + 1):
    t_i, x_i, y_i = (int(x) for x in input().split())
    t.append(t_i)
    x.append(x_i)
    y.append(y_i)

for i in range(N):
    t_diff = t[i + 1] - t[i]
    x_diff = abs(x[i + 1] - x[i])
    y_diff = abs(y[i + 1] - y[i])
    if (t_diff % 2) + ((x_diff + y_diff) % 2) == 1:
        print("No")
        sys.exit()
    else:
        if t_diff < x_diff + y_diff:
            print("No")
            sys.exit()
print("Yes")
