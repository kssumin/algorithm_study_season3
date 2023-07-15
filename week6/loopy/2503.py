N = int(input())

result = 0

mark = [[False, False] for _ in range(1000)]

for i in range(N):
  state, strike, ball = list(map(int, input().split()))

  for j in range(100, 1000):
    j = str(j)
    if j[0] == j[1] or j[1] == j[2] or j[2] == j[0]:
      continue
    if j[0] == '0' or j[1] == '0' or j[2] == '0':
      continue

    s, b = 0, 0
    for k in range(3):
      if j[k] == str(state)[k]:
        s += 1
      elif j[k] in str(state):
        b += 1

    if s == strike and b == ball:
      mark[int(j)][0] = True
    else:
      mark[int(j)][1] = True
      mark[int(j)][0] = False

for i in range(100, 1000):
  if mark[i][0] and not mark[i][1]:
    result += 1

print(result )