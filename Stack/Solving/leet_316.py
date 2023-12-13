import collections

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         strset = set(s)
#         stack, counter = [], collections.Counter(s)
#         for ch in s:
#             counter[ch] -= 1
#             if ch in stack:
#                 continue
#             while stack and ch < stack[-1] and counter[stack[-1]] > 0:
#                 stack.pop()
#             stack.append(ch)

#         return ''.join(stack)

# s1 = Solution()
# print(s1.removeDuplicateLetters("bcabc"))

class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
      counter, seen, stack = collections.Counter(s), set(), []

      for char in s:
          # 개수는 하나씩 감소
          counter[char] -= 1

          # 이미 있는 문자이면 계속 진행
          if char in seen:
              continue

          # stack[-1]은 스택의 마지막 문자
          # 스택이 비어있지 않고, 현재 문자가 스택의 마지막 문자보다 사전순으로 앞에 있고, 스택의 마지막 문자가 뒤에 또 있다면
          while stack and char < stack[-1] and counter[stack[-1]] > 0:
              # 스택에서 해당 문자를 제거
              seen.remove(stack.pop())
          
          stack.append(char)
          seen.add(char)

      return ''.join(stack)

s1 = Solution()
# print(s1.removeDuplicateLetters("bcabc"))
print(s1.removeDuplicateLetters("cbacdcbc"))