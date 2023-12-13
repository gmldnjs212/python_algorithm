import string
from pprint import pprint

text = 'hello, this is sparta'

counter = {}
# 21 번 연산
for char in text:
    # 알파벳이 아니면 패스
    if not char.isalpha():
        continue
    # 알파벳이라면 다음 수행
    if char in counter:
        # 이미 딕셔너리에 있으면 1 추가
        counter[char] += 1
    else:
        # 아니라면 새로추가하고 1 할당
        counter[char] = 1
# print인데 좀더 이쁘게 출력됨
pprint(counter)

# 일부로 복잡하게 푼 케이스
counter2 = {}
# 26 * 21 번 연산
for lo in string.ascii_lowercase:
    for char in text:
        if lo == char:
            if lo in counter2:
                counter2[lo] += 1
            else:
                counter2[lo] = 1
pprint(counter2)
