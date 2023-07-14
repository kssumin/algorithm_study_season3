import sys
input = sys.stdin.readline

N = int(input())
pillar_list = []

for i in range(N):
    L, H = map(int, input().split())
    pillar_list.append((L, H))
pillar_list.sort()
max_height, max_index = 0, 0
for i in range(N):
    height = pillar_list[i][1]
    if height >= max_height:
        max_height = height
        max_index = i
#max_height = max(pillar_list, key=lambda x: x[1])
result = pillar_list[max_index][1]
start_index, end_index = 0, 0
for i in range(1, max_index + 1):
    if pillar_list[i][1] >= pillar_list[end_index][1]:
        end_index = i
        result += (pillar_list[end_index][0] - pillar_list[start_index][0]) * pillar_list[start_index][1]
        start_index = end_index
start_index, end_index = N-1, N-1
for i in range(N-1, max_index-1, -1):
    if pillar_list[i][1] >= pillar_list[end_index][1]:
        end_index = i
        result += (pillar_list[start_index][0] - pillar_list[end_index][0]) * pillar_list[start_index][1]
        start_index = end_index
print(result)

"""
이 문제는 잘 풀렸다.
그냥 생각난 대로 풀어보니까 통과했다.
"""