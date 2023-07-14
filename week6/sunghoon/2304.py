'''
/*문제 정보 */
2304번 - 창고 다각형
난이도 - 실버 2
/*풀이 방법 */
2차원 리스트로 주어진 값을 받아주고 1차원 기준으로 정렬한 뒤 최대 높이 기둥 인덱스를
찾아주고 최대 높이 기둥을 기준으로 왼쪽 넓이, 오른쪽 넓이, 최대기둥 넓이를 더해
값을 구해주었다.
'''
import sys
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    a, b = map(int, input().split())
    li.append([a, b])

li.sort()
max_index = 0
a = 0
for i in li:
    if i[1] >= a:
        a = i[1]
        max_index = li.index(i)

result = li[max_index][1]
b = li[0][1]

for i in range(0, max_index, 1):
    if b <= li[i+1][1]:
        result += (li[i+1][0] - li[i][0]) * b
        b = li[i+1][1]

    else:
        result += (li[i+1][0] - li[i][0]) * b

b = li[-1][1]

for i in range(n-1, max_index, -1):
    if b < li[i - 1][1]:
        result += b * (li[i][0] - li[i - 1][0])
        b = li[i - 1][1]
    else:
        result += b * (li[i][0] - li[i - 1][0])

print(result)
'''
/*오답 노트*/
/*느낀 점*/
처음에 [0] * 1001 에 주어진 값을 넣어 1차원으로 풀어봤는데, 조건을 달아줘야하는게
꽤 많았고 넓이를 구해가는 과정이 2차원으로 하는 것보다 더 복잡해져서 2차원으로 풀었다.
요즘 계절로 파이썬 듣는데, 그 수업이 나름 도움이 되는 것 같다.
'''