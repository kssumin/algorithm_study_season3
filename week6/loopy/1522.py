s = input()

countA = s.count('a')
minB = 10000

s += s[:countA - 1]
for i in range(len(s) - countA + 1):
    minB = min(minB, s[i:i+countA].count('b'))

print(minB)
