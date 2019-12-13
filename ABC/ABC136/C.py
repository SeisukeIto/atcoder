import sys
N = int(input())
height = list(map(int, input().split()))
pre_h = 0
now_h = height[0]

for i in range(1, N):
    next_h = height[i]
    if now_h > next_h:
        now_h -=1
        if now_h > next_h or pre_h > now_h:
            print("No")
            sys.exit()
    elif now_h > pre_h:
        now_h -= 1
    pre_h = now_h
    now_h = next_h
print("Yes")
