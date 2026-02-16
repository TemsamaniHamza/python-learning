from typing import List

class Solution:
    def pitotal(self, b: List[int], i:int) -> int:
        tot = 1
        for j in range(len(b)):
            if i != j:
                tot *= b[j]
        return tot
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(self.pitotal(nums, i))
        return ret
    

s = Solution()

print(s.productExceptSelf([1,2,3,4]))
