s = input()
odd = ["R", "U", "D"]
even = ["L", "U", "D"]
for i in range(len(s)):
    if i%2 == 0:
        if s[i] in odd:
            continue
        else:
            print("No")
            break
    elif i%2 == 1:
        if s[i] in even:
            continue
        else:
            print("No")
            break
else:
    print("Yes")
