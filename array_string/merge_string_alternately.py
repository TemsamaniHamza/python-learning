class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = str()
        for i in range(len(word1)):
            s += word1[i]
            if i < len(word2):
                s += word2[i]
        s += word2[i+1:len(word2)]
        return s

s = Solution()
# a b c d e f

print(s.mergeAlternately("ace","bdfhamza"))