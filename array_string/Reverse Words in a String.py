from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:    
        words = deque(s.split())
        out = []
        while words:
            out.append(words.pop())
        return " ".join(out)

            

s = Solution()
print(s.reverseWords("hello world this is fine"))