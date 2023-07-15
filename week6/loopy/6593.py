
L, R, C = list(map(int, input().split()))

while(L != 0 and R != 0 and C != 0):
  building = []
  for i in range(L):
      floor = []
      for j in range(R):
          floor.append(list(input()))
      input()
      building.append(floor)

  for i in range(L):
      for j in range(R):
          for k in range(C):
              if building[i][j][k] == 'S':
                  start = (i, j, k)
              elif building[i][j][k] == 'E':
                  end = (i, j, k)

  visited = [[[False] * C for _ in range(R)] for _ in range(L)]

  queue = [start]
  visited[start[0]][start[1]][start[2]] = True

  isFinish = False

  result = 0
  while queue:
      result += 1
      for _ in range(len(queue)):
          x, y, z = queue.pop(0)
          for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)]:
              nx, ny, nz = x + dx, y + dy, z + dz
              if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C:
                  continue
              if building[nx][ny][nz] == '#':
                  continue
              if visited[nx][ny][nz]:
                  continue
              if (nx, ny, nz) == end:
                  print(f"Escaped in {result} minute(s).")
                  isFinish = True
                  break
              visited[nx][ny][nz] = True
              queue.append((nx, ny, nz))
          if isFinish:
              break
      if isFinish:
          break
  if not isFinish:
    print("Trapped!")
  L, R, C = list(map(int, input().split()))