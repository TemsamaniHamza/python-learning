from collections import deque

class Solution:
    def reverseVowels(self, s: str) -> str:
        d = deque()
        vowels = set("aeiouAEIOU")
        s_list = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                d.append(i)
        while len(d) > 1:
            i = d.popleft()
            j = d.pop()
            s_list[i], s_list[j] = s_list[j], s_list[i]

        return "".join(s_list)

s = Solution()

str = "abce"
print(s.reverseVowels(str))
