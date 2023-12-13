import string


def solution(S):
    for el in list(string.ascii_lowercase):
        if el in S:
            print(f"{S.find(el)}", end=' ')
        else:
            print("-1", end=' ')


def solution2(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1] * len(string.ascii_lowercase)
    for i in range(len(word)):
        # 아스키 코드 사용 ( 문자 -> 숫자 )
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))


solution('baekjoon')
solution2('baekjoon')
