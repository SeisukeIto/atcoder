a, b, c, d = map(int, input().split())

def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

mc = b // c - (a-1) // c
md = b // d - (a-1) // d
mcd = b // (c*d//gcd(c, d)) - (a-1) // (c*d//gcd(c, d))

print(int((b - a + 1) - mc - md + mcd))
