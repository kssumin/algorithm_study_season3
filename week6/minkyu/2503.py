from itertools import permutations
import sys
input = sys.stdin.readline
def throw(example_num):
    for i in range(1, N + 1):
        strike, ball = 0, 0
        for j in range(3):
            if throw_list[i][0][j] == example_num[j]:
                strike += 1
            for k in range(3):
                if k == j:
                    continue
                if throw_list[i][0][k] == example_num[j]:
                    ball += 1
        if not(strike == throw_list[i][1] and ball == throw_list[i][2]):
            return False
    return True

N = int(input())
throw_list = [[]]
for _ in range(N):
    num, strike, ball = map(int, input().split())
    num = str(num)
    throw_list.append([num, strike, ball])

result = 0
for numbers in permutations(range(1, 10), 3):
    n1, n2, n3 = map(str, numbers)
    example_num = n1 + n2 + n3
    if throw(example_num):
        result += 1
print(result)

"""
처음에 백트래킹으로 구현하려고 했는데 코드가 너무너무너무 길어지고 복잡해져서 이건 아니다 싶어서 무슨 알고리즘 분류를 봤다.
알고보니 브루트포스라서 그냥 모든 경우의 수를 다 때려넣어보면 됐다.
모든 경우의 수를 다 해보는 건 시간이 오래 걸릴 거 같아서 생각하지 않았는데
999 * 4 정도로 경우의 수가 적어서 그런가 브루트포스로 통과했다.
"""