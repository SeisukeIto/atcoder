import sys
a, b = map(int, input().split())
i = 1
if b == 1:
    print(0)
    sys.exit()

while True:
    if b <= (a-1)*i + 1:
        print(i)
        break
    i += 1
