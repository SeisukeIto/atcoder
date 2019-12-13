import math
a, b = map(int, input().split())
ans = {1}

def calc_gcd(x, y):
    if y == 0: return x
    return calc_gcd(y, x%y)

def factrize(z):
    i = 2
    set = {1}
    while i*i <= z:
        while z%i==0:
            z//=i
            set.add(i)
        i+=1
    if z > 1:
        set.add(z)
    return set

gcd = calc_gcd(a, b)
print(len(factrize(gcd)))
