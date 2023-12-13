# https://leetcode.com/problems/array-partition/

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a = 0
        for i in range(0, len(nums), 2):
            a += nums[i]
        return a


s1 = Solution()
s1.arrayPairSum(nums=[1, 4, 3, 2])
s1.arrayPairSum(nums=[6, 2, 6, 5, 1, 2])
