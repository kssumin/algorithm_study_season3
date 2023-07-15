N = int(input())

lines = [0] * 1000

for i in range(N):
    L, H = list(map(int, input().split()))
    lines[L-1] = H

maxHeight = max(lines)

lastHeight = 0
startIndex = 0
for i in enumerate(lines):
    if i[1] == maxHeight:
        startIndex = i[0]
        break
    if i[1] > lastHeight:
        lastHeight = i[1]
    else:
        lines[i[0]] = lastHeight

lastHeight = 0
endIndex = 0
for i in range(len(lines)-1, -1, -1):
    if lines[i] == maxHeight:
        endIndex = i
        break
    if lines[i] > lastHeight:
        lastHeight = lines[i]
    else:
        lines[i] = lastHeight

if not startIndex == endIndex:
    for i in range(startIndex, endIndex):
        lines[i] = maxHeight

print(sum(lines))