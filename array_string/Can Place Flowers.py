from typing import List
class Solution:
    def check_neighbors(self, b: List[int], n: int, i: int) -> bool:
        if i != 0:
            if b[i-1] != 0:
                return False
        if i != len(b) - 1:
            if b[i+1] != 0:
                return False
        return True
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i , val in enumerate(flowerbed):
            if (val == 0):
                if self.check_neighbors(flowerbed,n,i):
                        flowerbed[i] = 2
        if flowerbed.count(2) < n:
            return False
        return True
    
s  = Solution()
print(s.canPlaceFlowers([0,0,1,0,1,0], 1))