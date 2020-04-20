N = int(input())
S = input()
r = S.count('R')
g = S.count('G')
b = S.count('B')
c = 0
for i in range(N-2):
  for j in range(i+1,(i+N+1)//2):
    k = j*2-i
    if len(set([S[i], S[j], S[k]]))==3:
      c += 1
print(r*g*b-c)
