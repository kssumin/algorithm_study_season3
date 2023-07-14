'''
/*문제 정보 */
1522번 - 문자열 교환
난이도 - 실버 1
/*풀이 방법 */
주어진 문자열에서 a가 연속이기 위해서 a의 개수만큼 슬라이싱하여 그 범위 안에 b개수
를 구해주는 방식으로 풀었다. 반복문을 통해 최솟값 갱신을 해주었다.
'''
import sys
input = sys.stdin.readline

li = input().rstrip()
a = li.count('a')
result = 1001

li += li[0:a-1]
for i in range(len(li)-(a-1)):
    result = min(result, li[i:i+a].count('b'))

print(result)

'''
/*오답 노트*/
오답 노트 1. 문자열 원형 처리 해주기
li += li[0:a-1] 를 추가해 주었다.
/*느낀 점*/

오답 노트 2. rstrip()
input을 받을 때, rstrip()을 해주지 않아 5번 오류 .....

'''