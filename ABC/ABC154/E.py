import math

def csum(a):
    if a == 1:
        return 1
    else:
        return a*(a+1)//2

n = int(input())
k = int(input())
nstr = str(n)
nlen = len(nstr)
ans = 0

if k == 1:
    ans += 9*(nlen-1)
    ans += int(nstr[0])
elif k==2:
    if nlen < 2:
        pass
    elif nlen == 2:
        ans += (int(nstr[0])-1)*9
        ans += int(nstr[1])
    else:
        ans += 9*9*(csum(nlen-2))
        ans += (int(nstr[0])-1)*9*(nlen-1)
        hoge = 0
        for i in range(1, nlen):
            hoge+=int(nstr[i])
        ans += hoge

print(ans)
