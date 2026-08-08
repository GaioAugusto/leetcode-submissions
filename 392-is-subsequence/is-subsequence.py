class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        for i in reversed(t):
            if len(s) == 0:
                return True
            if s[-1] == i:
                s.pop()
        return True if len(s) == 0 else False