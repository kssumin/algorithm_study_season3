import sys
input = sys.stdin.readline


def change(letter):
    tmp = list(letter)
    result = []
    for i in range(len(tmp)):
        if tmp[i] == 'n' and i != len(tmp) - 1:
            if tmp[i + 1] == 'g':
                result.append(min_dict['ng'])
            else:
                result.append(min_dict[tmp[i]])
        elif tmp[i] == 'g' and i != 0:
            if tmp[i-1] == 'n':
                pass
            else:
                result.append(min_dict[tmp[i]])
        else:
            result.append(min_dict[tmp[i]])
    return result

N = int(input())
min_language = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']
min_dict = {}
for i in range(len(min_language)):
    min_dict[min_language[i]] = i

letter_list = []
for _ in range(N):
    letter = input().rstrip()
    letter_list.append((letter, change(letter)))
letter_list.sort(key=lambda x: x[1])
for i in range(N):
    print(letter_list[i][0])

"""
민식어에 숫자를 매기고 그걸로 sort를 했다.
처음에는 sort 함수를 오버라이드 해서 어떻게 바꿀 수 있지 않을까 생각했는데 어떻게 해야할지 모르겠다.
찾아보니 오버라이드하지 않고 그냥 sort 함수의 key에 cmp_to_key메소드에 직접 만든 함수를 넣으면 됐다.
정렬 기준을 내 맘대로 정할 수 있다.
"""