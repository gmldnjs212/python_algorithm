# https://leetcode.com/problems/3sum/

from typing import List

# 입력받은 배열에 있는 세 요소의 합이 0이 되는 케이스를 찾는 문제
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ret = []
        nums.sort()

        for i in range(len(nums)):

            # for문을 돌며 중복 값이 나오는 경우는 제외시킵니다.
            # i가 1인 경우 부터 시작합니다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # left와 right를 포인터같이 활용합니다.
            left, right = i + 1, len(nums) - 1
            while left < right:

                # 세 수의 합을 val에 할당하여 문제에서 제시한 조건에 만족하는지 판단할 예정입니다.
                val = nums[i] + nums[left] + nums[right]
                
                if val > 0:
                    right -= 1

                elif val < 0:
                    left += 1

                else:
                    # val이 0인 경우에는 조건에 만족하는 케이스이므로 해당조합을 ret에 저장합니다.
                    ret.append([nums[i], nums[left], nums[right]])

                    # left 포인터가 그 다음 값과 중복인 케이스를 제외시키는 코드입니다. ( left와 left의 +1 인덱스인 값을 비교 )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # right 포인터가 그 다음 값과 중복인 케이스를 제외시키는 코드입니다. ( right와 right의 -1 인덱스인 값을 비교 )
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 왜 하는지 이해 못함
                    left += 1
                    right -= 1

        return ret


s1 = Solution()
print(f"example 1 : {s1.threeSum(nums=[-1, 0, 1, 2, -1, -4])}")
print(f"example 2 : {s1.threeSum(nums=[0, 1, 1])}")
print(f"example 3 : {s1.threeSum(nums=[0, 0, 0])}")
