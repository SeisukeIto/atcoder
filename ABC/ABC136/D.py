S = input()
now = "R"
now_num = 0
my_list = []

for i in range(len(S)):
    if S[i] == "R":
        if now == "L":
            my_list.append(now_num)
            now = "R"
            now_num = 1
        else:
            now_num += 1
    elif S[i] == "L":
        if now == "R":
            my_list.append(now_num)
            now = "L"
            now_num = 1
        else:
            now_num += 1
my_list.append(now_num)

for i in range(0, len(my_list), 2):
    for j in range(my_list[i] - 1):
        print(0, end =" ")
    sum = my_list[i] + my_list[i + 1]
    if sum % 2 == 0:
        print(sum // 2, end =" ")
        print(sum // 2, end =" ")
    elif my_list[i] % 2 == 0:
        print(sum // 2, end =" ")
        print(sum // 2 + 1, end =" ")
    else:
        print(sum // 2 + 1, end =" ")
        print(sum // 2, end =" ")
    for j in range(1, my_list[i + 1]):
        print(0, end =" ")
