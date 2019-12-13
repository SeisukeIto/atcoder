n = int(input())
s = input()

if n%2 == 1:
    print('No')
else:
    for i in range(n//2):
        if not s[i] == s[i+n//2]:
            print('No')
            break
    else:
        print('Yes')
