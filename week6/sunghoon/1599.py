'''
/*문제 정보 */
1599번 - 민식어
난이도 - 골드 5
/*풀이 방법 */
코드 리뷰 했습니다.
https://richard25.tistory.com/67
'''

import sys
input = sys.stdin.readline
minSick = {"a": "A", "b": "B", "k": "C",
           "d": "D", "e": "E", "g": "F",
           "h": "G", "i": "H", "l": "I",
           "m": "J", "n": "K",
           "o": "M", "p": "N", "r": "O",
           "s": "P", "t": "Q", "u": "R",
           "w": "S", "y": "T"
           }
# 보다 확실한 구분을 위하여 대문자로 변환하였습니다.

def changeMinSick(word):      # 우선 ng 를 l 로 바꿔주고
    result = word.replace("ng", "L")
    for k, v in minSick.items():         # 키 값을 가져와 바꿔준다.
        result = result.replace(k, v)
    return result


def soluction(array):
    result = dict()
    for i in array:
        temp = changeMinSick(i)
        result[i] = temp
    result = sorted(result.items(), key=lambda x: x[1])
    return result


if __name__ == "__main__":
    array = []
    N = int(input())
    for _ in range(N):
        array.append(input().rstrip())
    answer = soluction(array)
    for i in answer:
        print(i[0])
'''
/*오답 노트*/
/*느낀 점*/

'''