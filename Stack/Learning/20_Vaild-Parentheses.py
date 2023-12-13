class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {
            '}' : '{',
            ']' : '[',
            ')' : '(',
        }
        opener = "({["
        stack = []

        for char in s:
            # opener가 나왔는지 확인
            # true라면 순서대로 stack에 쌓이게 됨
            if char in opener:
                stack.append(char)
            # char가 opener가 아니라면? > closer가 나와야함
            else:
                # closer가 나와야 하는데 stack이 비어있는경우 > False
                if not stack:
                    return False
                top = stack.pop()
                # opener에 해당하는 closer가 top으로 나온애랑 같은지 확인
                if pair[char] != top:
                    return False
        # 반환하기 전에 stack에 값이 남아있는지 확인
        # for문을 돌며 위 조건을 모두 만족해도 값이 남아있는 경우가 있다.
        # 예시 : {{}}]] 같은 경우
        return not stack
    
s1 = Solution()
print(s1.isValid(s = "()")) # true
print(s1.isValid(s = "()[]{}")) # true
print(s1.isValid(s = "(]")) # false