class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Sum array elements
        sum = 0
        for num in nums:
            sum += num
        return sum % k