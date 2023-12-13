class Solution(object):
    def dailyTemperatures(self, temp):
      """
      :type temperatures: List[int]
      :rtype: List[int]
      """
      ans = [0] * len(temp) # [0]이 temp의 요소 개수만큼 생성
      stk = []

      for i, v in enumerate(temp): # i: 인덱스값 , v: temp값
        while stk and temp[stk[-1]] < v: # stk에 값이 있어야함 + 이전값이 현재값보다 작아야함
          last = stk.pop() # stk에서 맨 마지막 값(=인덱스) 추출
          ans[last] = i - last # ans에 이전 인덱스값을 현재 인덱스 - 이전인덱스로 처리
        stk.append(i) # stk에 i를 추가

      return ans


s1 = Solution()
s1.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
s1.dailyTemperatures(temperatures = [30,40,50,60])
s1.dailyTemperatures(temperatures = [30,60,90])