n = int(input())
a_lst = [0]*n
a_lst[0] = int(input())
a_lst[1] = int(input())
if a_lst[0] >= a_lst[1]:
    max = 0
    sec_max = 1
else:
    max = 1
    sec_max = 0

for i in range(2, n):
    a_lst[i] = int(input())
    if a_lst[i] > a_lst[max]:
        max = i
    elif a_lst[i] > a_lst[sec_max]:
            sec_max = i

for i in range(n):
    if i == max:
        print(a_lst[sec_max])
    else:
        print(a_lst[max])
