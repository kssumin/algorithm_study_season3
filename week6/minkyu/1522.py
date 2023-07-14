import sys
input = sys.stdin.readline
INF = sys.maxsize

letter = list(input().rstrip())
count_letter = len(letter)
count_a = letter.count('a')
count_b = INF

for i in range(count_letter):
    if i + count_a <= count_letter:
        tmp_count = letter[i:i+count_a].count('b')
    else:
        tmp_count = letter[i:count_letter].count('b') + letter[:count_a - (count_letter - i)].count('b')
    count_b = min(count_b, tmp_count)
print(count_b)

"""
와 이건 진짜 모르겠어서 질문 게시판에서 힌트를 봤는데도 못 풀었다.
블로그 가서 어떻게 푸는 건지만 보고 코드를 짰다.
a가 들어갈 구간을 정해놓고 거기서 b의 개수를 세면 그 b를 a와 바꾸면 되니 b의 개수가 최소인 구간을 찾으면 된다.
"""