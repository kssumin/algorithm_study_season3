'''
문제 : 창고 다각형
난이도 : 실버2

어디가 
'''
import sys
import copy

n = int(sys.stdin.readline())
heights = []
for _ in range(n):
    l, h = map(int, sys.stdin.readline().split())
    heights.append((l, h))

heights = sorted(heights, key=lambda x: x[0])
keypoint = copy.deepcopy(heights)

max = heights[0][1]
for i in range(1, len(heights)):
    if (heights[i][1] <= max):
        keypoint.remove(heights[i])
    else:
        max = heights[i][1]

answer = 0
for j in range(len(keypoint)-1):
    answer += (keypoint[j+1][0] - keypoint[j][0]) * keypoint[j][1]
answer += keypoint[-1][1]

if (keypoint[-1][0] != heights[-1][0]):
    answer += (heights[-1][0] - keypoint[-1][0]) * heights[-1][1]
print(answer)
