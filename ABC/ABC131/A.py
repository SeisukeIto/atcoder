s = list(input())
pre = s[0]

for i in range(1, 4):
    if pre == s[i]:
        print("Bad")
        break
    else:
        pre = s[i]
        if i == 3:
            print("Good")
            break
