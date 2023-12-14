# 노드 생성
class Node:
  def __init__(self, item, next):
    self.item = item
    self.next = next


class Queue:
  def __init__(self):
    self.front = None

  def is_empty(self):
    return self.front is None
  
  def push(self, value):
    # 비었다면
    if not self.front:
      # 노드를 넣어주고 종료
      self.front = Node(value, None)
      return
    
    # 안 비었다면
    node = self.front
    # 일단 끝까지 감
    while node.next:
      node = node.next
    # 끝에 노드 생성
    node.next = Node(value, None)

    def pop(self):
      # 비었다면
      if not self.front:
        # None 뱉고 종료
        return None
      
      # 안 비었다면
      # 첫 노드를 꺼내서 node.item을 반환한다
      # 그 다음노드를 첫 노드로 지정한다.
      node = self.front
      self.front = self.front.next
      return node.item