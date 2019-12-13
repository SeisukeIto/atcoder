from math import factorial
x, y = map(int, input().split())
m = 10**9+7

if not (x+y)%3==0:
    print(0)
else:
    a = (2*x-y)//3
    b = (2*y-x)//3
    ans = factorial(a+b)//(factorial(a)*factorial(b))
    print(int(ans%m))
