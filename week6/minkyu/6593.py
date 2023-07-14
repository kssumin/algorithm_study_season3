import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while 1:
    L, R, C = map(int, input().split())
    building = [[] for _ in range(L)]
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    if L == 0 and R == 0 and C == 0:
        break
    for i in range(L):
        for _ in range(R):
            building[i].append(list(input().rstrip()))
        Enter = input()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    start = [i, j, k, 0]

    queue = deque([start])
    visited[start[0]][start[1]][start[2]] = True
    while queue:
        z, x, y, r = queue.popleft()
        if building[z][x][y] == 'E':
            print('Escaped in {} minute(s).'.format(r))
            break
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    queue.append([nz, nx, ny, r + 1])
    else:
        print('Trapped!')

"""
그냥 bfs에 z축만 추가된 문제다.
그런데 bfs를 너무 오랜만에 풀었는지 bfs에서 가장 중요한 것 중에 하나인 popleft를 안하고 pop을 해서 계속 틀렸었다.
bfs에 익숙해졌다고 생각했는데 전에 했던 알고리즘도 다시 복습을 해야겠다.
"""