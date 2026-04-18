class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            result = 0
            while n > 0:
                remainder = n % 10
                result = result*10 + remainder
                n = n // 10
            return result
        
        return abs(n - reverse(n))