class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        result = ""
        while len(result) < len(word1) + len(word2):
            if p1 >= len(word1):
                result += word2[p2:]
                return result
            if p2 >= len(word2):
                result += word1[p1:]
                return result
            
            if p1 <= p2:
                result += word1[p1]
                p1 += 1
            else:
                result += word2[p2]
                p2 += 1
        # return result