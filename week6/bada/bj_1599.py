'''
문제 : 민식어
난이도 : 골드5
'''
import sys
from functools import cmp_to_key
input = sys.stdin.readline


def compare(a, b):
    length = min(len(a), len(b))
    for i in range(length):
        if minsik.index(a[i]) == minsik.index(b[i]):
            continue
        else:
            if minsik.index(a[i]) > minsik.index(b[i]):
                return 1
            else:
                return -1

    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    else:
        return 0


minsik = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l',
          'm', 'n', 'z', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']

n = int(input())
words = []

for _ in range(n):
    w = input().strip()
    w = w.replace("ng", "z")
    words.append(w)

words = sorted(words, key=cmp_to_key(compare))

for w in words:
    print(w.replace("z", "ng"))
