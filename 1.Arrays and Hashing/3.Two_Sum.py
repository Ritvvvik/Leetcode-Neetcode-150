from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        L = 0
        while(L<n):
            R = L+1
            while(R<n):
                if nums[L] + nums[R] == target:
                    return [L,R]
                else:
                    R+=1
            L+=1
        