# https://velog.io/@ny_/%EB%B0%B1%EC%A4%80-1874%EB%B2%88.-%EC%8A%A4%ED%83%9D-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://www.youtube.com/watch?v=byCxMbgzEVM


count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())

    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
        
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)