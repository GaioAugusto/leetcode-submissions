class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        new_string = ""
        for i in range(k-1,-1,-1):
            new_string += s[i]
        
        for i in range(k, len(s)):
            new_string += s[i]

        return new_string
