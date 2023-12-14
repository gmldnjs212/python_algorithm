class MyCircularQueue(object):

  def __init__(self, k):
    """
    :type k: int
    """
    self.q = [None] * k
    self.maxlen = k
    self.frontIdx = 0
    self.rearIdx = 0

  def enQueue(self, value):
    if self.q[self.rearIdx] is None:
      self.q[self.rearIdx] = value
      self.rearIdx = (self.rearIdx+1) % self.maxlen
      return True

    else:
      return False

  def deQueue(self):
    if self.q[self.frontIdx] is None:
      return False

    else:
      self.q[self.frontIdx] = None
      self.frontIdx = (self.frontIdx+1) % self.maxlen
      return True


  def Front(self):
    return -1 if self.q[self.frontIdx] is None else self.q[self.frontIdx]

  def Rear(self):
    return -1 if self.q[self.rearIdx-1] is None else self.q[self.rearIdx-1]
    

  def isEmpty(self):
    return self.frontIdx == self.rearIdx and self.q[self.frontIdx] is None


  def isFull(self):
    return self.frontIdx == self.rearIdx and self.q[self.frontIdx] is not None
