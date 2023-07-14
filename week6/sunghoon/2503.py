'''
/*문제 정보 */
2503번 - 숫자 야구
난이도 - 실버 3
/*풀이 방법 */
순열 라이브러리를 이용해 strike 와 ball 값이 다르면 제거해 주는 방식으로 풀었다.
도저히 정답이 나오지 않아 블로그 참조했다.
https://yuna0125.tistory.com/115
'''
from itertools import permutations

N = int(input())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(N):
    n, s, b = map(int, input().split())
    n = list(str(n))
    rmcnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= rmcnt  # num[0] 부터 시작
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b):
            num.remove(num[i])
            rmcnt += 1

print(len(num))
'''
/*오답 노트*/
오답 노트 1. 예제 1번 728 출력
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
li = [list(permutations([1,2,3,4,5,6,7,8,9],3))]
st, ball = 0,0
count = 0
for _ in range(n):
    a, s, b = map(int, input().split())
    a = list(str(a))


    for te in li:
        for i in range(3):
            if te[i] == a[i]:
                st += 1
            elif a[i] in te[i]:
                ball += 1
        if (st != s) or (ba != b):
            li.remove(te)
            count += 1
print(729 - count)

/*느낀 점*/
알고리즘 문제를 풀 때, 사소하게 잘못한 부분 찾는 것이 너무 어렵당...
전체적인 방향 찾는 것에서 이미 힘 다빠지는데 오답까지 나오면 너무 지친다..
'''