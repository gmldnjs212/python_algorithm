from collections import Counter

class Solution(object):
  def removeDuplicateLetters(self, s):
    count = Counter(s)
    stack = []
    seen = set()

    for c in s:
      count[c] -= 1

      if c in stack:
        continue

      # stack이 비어있으면 안되고
      # stack 최상단의 문자가 c보다 작아야하고
      # stack 최상단의 문자의 남은 개수가 1개이상이어야 한다.
      while stack and c < stack[-1] and count[stack[-1]]>0:
        removed = stack.pop()
        seen.remove(removed)

      stack.append(c)
      seen.add(c)

    return ''.join(stack)

s1 = Solution()
s1.removeDuplicateLetters("bcabc")
s1.removeDuplicateLetters("cbacdcbc")