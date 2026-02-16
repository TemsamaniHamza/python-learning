from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies)
        arr = []
        for i, n in enumerate(candies):
            if(n + extraCandies >= x):
                arr.append(True)
            else:
                arr.append(False)
        return arr

s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
# a = [5, 9, 4]

# b = a[:]
# b.sort(reverse=True)
# print(a)