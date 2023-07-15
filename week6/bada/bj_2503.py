import sys
from itertools import permutations
n = int(input())
n_list = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    n_list.append(a)

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i_list = list(permutations(items, 3))
cnt = 0
for a in i_list:
    flag = 0
    for i in range(n):
        s, b = 0, 0
        num_str = list(map(int, str(n_list[i][0])))
        for j in range(3):
            if a[j] == num_str[j]:
                s += 1
            else:
                if a[j] in num_str:
                    b += 1
        if s != n_list[i][1] or b != n_list[i][2]:
            flag = 0
            break

        else:
            flag = 1
    if flag == 1:
        cnt += 1
print(cnt)
