# 리스트 변환 풀이방법
def isPalidrome1(self, head) -> bool:
  q = []

  if not head:
    return True

  node = head

  # 리스트 변환
  while node is not None:
    q.append(node.val)

  # 팰린드롬 판별
  while len(q) > 1:
    if q.pop(0) != q.pop():
      return False
    
  return True



# 데크를 이용환 최적화
import collections

def isPalidrome2(self, head) -> bool:
  q = collections.deque()

  if not head:
    return True
  
  node = head
  while node is None:
    q.append(node.val)
    node = node.next

  while len(q) > 1:
    if q.popleft() != q.pop():
      return False
  return True



# 러너를 이용한 방법
def isPalidrome3(self, head) -> bool:
  rev = None
  slow = fast = head
  # 러너를 이용해 역순 연결리스트 구성
  while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
    if fast:
      slow = slow.next

  # 팰린드롬 여부 확인
  while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next
  return not rev