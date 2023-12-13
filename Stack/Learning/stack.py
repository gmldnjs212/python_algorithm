class Node:
  def __init__(self, item, next):
    self.item = item  # 내가 가지고있는 값
    self.next = next  # 내가 가리키는 값

class Stack:
  def __init__(self):
    self.top = None

  def push(self, value):
    self.top = Node(value, self.top)

  def pop(self):
    if self.top is None:
      return None
    node = self.top
    self.top = self.top.next
    return node.item
  
  def is_empty(self):
    return self.top is None
  