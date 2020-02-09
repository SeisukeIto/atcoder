import sys
sys.setrecursionlimit(1000000)
import fractions
from functools import reduce

mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y/2)**2 * x % mod

def div(c, d):
    return mul(c, power(d, mod-2))

n = int(input())
a = tuple(map(int, input().split()))

def lcm_base(l, m):
    return (l * m) // fractions.gcd(l, m)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


a_lcm = lcm(*a)
ans = 0

for i in range(n):
    ans += div(a_lcm, a[i])%mod
    ans %= mod

print(ans)
