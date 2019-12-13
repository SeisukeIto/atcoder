s = input()
n = len(s)+1
num = 0
ans = 0
con = 0


for i in range(n-1):
    if s[i] == '>':
        if con == 0:
            con = 1
        else:
            con += 1

        num -= 1
        if num < 0:
            num = 0
            ans += con
    else:
        if not con == 0:
            ans = ans - num*(con)
            num = 0
        num += 1
        con = 0
    ans += num
print(ans)
