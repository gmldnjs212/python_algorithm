# Queue는 FIFO 구조
# enQueue : 삽입 (맨 뒤에 삽입)
# deQueue : 추출 (FIFO이니 맨 처음요소 부터 추출)


class MyCircularQueue(object):

  def __init__(self, k):
    self.q = [None] * k # k사이즈만큼 자리를 만들어둠
    self.maxlen = k # 입력받은 값이 사용할 수 있는 자리 개수임
    self.frontIdx= 0
    self.rearIdx = 0

  def enQueue(self, value):
    # rear가 가리키는 자리에 아무것도 없으면
    if self.q[self.p2] is None:

      # rear가 가리키는 자리에 value삽입
      self.q[self.p2] = value 

      # 다음자리로 p2 포인터를 이동
      # p2포인터가 maxlen을 넘어가면 나머지 연산
      self.rearIdx = (self.rearIdx+1) % self.maxlen
      return True
    # rear가 가리키는 자리에 값이 있다면
    else:
      # 삽입 실패
      return False


  def deQueue(self):      
    # front가 가리키는 곳에 아무것도 없으면
    if self.q[self.frontIdx] is None:

      # 추출 실패
      return False

      # front가 가리키는 곳에 있으면
    else:
      # front에 가리키는 곳에 있는 데이터를 삭제
      self.q[self.frontIdx] = None
      
      # maxlen을 넘어가면 나머지연산
      self.frontIdx = (self.frontIdx+1) % self.maxlen 
      return True


  def Front(self):
    # front가 가리키는 요소가 None이면 False를, 아니라면 그 값을 반환
    return -1 if self.q[self.frontIdx] is None else self.q[self.frontIdx]


  def Rear(self):
    # 맨 뒤의 요소를 반환 
    # (p2는 이미 뒤에 삽입될 자리를 가르키고 있기 때문에 
    # p2-1이 맨 뒤의 요소를 가르키고 있습니다.)
    return -1 if self.q[self.rearIdx-1] is None else self.q[self.rearIdx-1]


  def isEmpty(self):
    return self.frontIdx == self.rearIdx and self.q[self.frontIdx] is None


  def isFull(self):
    return self.frontIdx == self.rearIdx and self.q[self.frontIdx] is not None
      
