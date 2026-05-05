class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = []
        seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                queue.append(s[i])
            else:
                seen[s[i]] = -1
        
        for letter in queue:
            if seen[letter] != -1:
                return seen[letter]
        return -1