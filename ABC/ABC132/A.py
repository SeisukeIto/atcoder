s = input()
res_1 = 0
res_2 = 0
s_1 = s[0]
s_2 = None

for i in range(1, 4):
    if s[i] == s_1:
        res_1 += 1
    elif s[i] == s_2:
        res_2 += 1
    elif not s_2:
        s_2 = s[i]


if res_1 == 1 and res_2 == 1:
    print("Yes")
else:
    print("No")
